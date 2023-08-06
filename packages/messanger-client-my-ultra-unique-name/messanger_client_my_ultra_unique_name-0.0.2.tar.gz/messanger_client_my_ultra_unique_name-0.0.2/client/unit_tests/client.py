import json
import logging
import sys
import socket
import threading
import time
import traceback

from datetime import datetime
from sqlalchemy import or_

import logs.config.client_log_config

from config.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ENCODING, MAX_PACKAGE_LENGTH
from config.utils import get_message, send_message
from metaclasses import ClientVerifier
from client_database import create_session, Contact, MessageHistory

logger = logging.getLogger('client_logger')


def create_presence(account_name='Guest'):
    """
    Формирует запрос о присутствии клиента
    """
    logger.debug('Формируется запрос о присутствии клиента')
    out = {
        'action': 'presence',
        'time': datetime.now().strftime('%X %x'),
        'user': {
            'account_name': account_name
        }
    }
    return out


def process_ans(message):
    """
    Функция разбирает ответ сервера
    """
    logger.debug('Разбирается приветственный ответ сервера')
    if 'response' in message:
        if message['response'] == 200:
            return '200 : OK'
        return f'400 : {message["error"]}'
    raise ValueError


class ClientSender(threading.Thread, metaclass=ClientVerifier):

    def __init__(self, account_name, sock):
        self.account_name = account_name
        self.sock = sock
        super().__init__()

    @staticmethod
    def print_help():
        """Возможные действия юзера"""
        print('Выберите одну из команд:\n'
              'm - отправить сообщение. Кому и текст будет запрошены отдельно\n'
              'history - история сообщений\n'
              'help - вывести подсказки по командам\n'
              'users - список пользователей\n'
              'con - действия с контактами\n'
              'q - выход из программы')

    def get_contacts(self):
        user_request = {
            'action': 'get_contacts',
            'time': datetime.now().strftime('%X %x'),
            'user_login': self.account_name
        }
        logger.debug(f'Отправляю запрос пользователей к серверу')
        try:
            send_message(self.sock, user_request)
        except Exception:
            logger.critical(f'Ошибка отправки\n{traceback.format_exc()}')

    def message_history(self):
        action = input('Какие сообщения вы хотите посмотреть?\n'
                       'in - входящие\n'
                       'out - исходящие\n'
                       'all - удалить контакт\n')
        while True:
            session = create_session()
            if action == 'in':
                messages = session.query(MessageHistory).filter(
                    MessageHistory.to_user_name == self.account_name).order_by(
                    MessageHistory.date).all()
                for i in messages:
                    print(f'От {i.from_user_name}: {i.message}')
                session.close()
                break
            elif action == 'out':
                messages = session.query(MessageHistory).filter(
                    MessageHistory.from_user_name == self.account_name).order_by(
                    MessageHistory.date).all()
                for i in messages:
                    print(f'Для {i.to_user_name}: {i.message}')
                session.close()
                break
            elif action == 'all':
                messages = session.query(MessageHistory).filter(
                    or_(MessageHistory.from_user_name == self.account_name,
                        MessageHistory.to_user_name == self.account_name)
                ).order_by(
                    MessageHistory.date).all()
                for i in messages:
                    print(f'От {i.from_user_name} для {i.to_user_name}: {i.message}')
                session.close()
                break
            else:
                print('Команда не распознана')
                continue

    def edit_contacts(self):
        action = input('Введите действие с контактами\n'
                       'l - список контактов\n'
                       'add - добавить контакт\n'
                       'del - удалить контакт\n')
        while True:
            session = create_session()
            if action == 'l':
                contacts = [i[0] for i in
                            session.query(Contact.contact_name).filter(Contact.owner_name == self.account_name).all()]
                for i in contacts:
                    print(i)
                session.close()
                break
            elif action == 'add':
                target = input('Введите имя пользователя: ')
                new_contact = Contact(owner_name=self.account_name, contact_name=target)
                session.add(new_contact)
                session.commit()
                session.close()
                print(f'Пользователь {target} добавлен в ваши контакты')
                break
            elif action == 'del':
                target = input('Введите имя пользователя: ')
                session.query(Contact) \
                    .filter(Contact.owner_name == self.account_name, Contact.contact_name == target) \
                    .delete()
                session.commit()
                session.close()
                print(f'Пользователь {target} удалён из ваших контактов')
                break
            else:
                print('Команда не распознана')
                continue

    def create_message(self):
        to_user = input('Введите получателя: ')
        message = input('Введите сообщение: ')
        message_dict = {
            'action': 'message',
            'time': datetime.now().strftime('%X %x'),
            'sender': self.account_name,
            'message_text': message,
            'destination': to_user
        }
        logger.debug(f'Сформирован словарь сообщения: {message_dict}')
        try:
            send_message(self.sock, message_dict)
            logger.info(f'Отправлено сообщение для пользователя {to_user}')
        except Exception:
            logger.critical(traceback.format_exc())
            logger.critical('Потеряно соединение с сервером.')
            sys.exit(1)

    # перегружаем ран от тредов
    def run(self):
        self.print_help()
        while True:
            command = input('Введите команду: ')
            if command == 'm':
                self.create_message()
            elif command == 'help':
                self.print_help()
            elif command == 'q':
                send_message(self.sock, {
                    'action': 'exit',
                    'time': datetime.now().strftime('%X %x'),
                    'account_name': self.account_name
                })
                logger.info('Завершение работы пользователем')
                # Задержка необходима, чтобы успело уйти сообщение о выходе
                time.sleep(0.5)
                break
            elif command == 'users':
                self.get_contacts()
            elif command == 'con':
                self.edit_contacts()
            elif command == 'history':
                self.message_history()
            else:
                logger.info('Команда не распознана')
                continue


class ClientReceiver(threading.Thread, metaclass=ClientVerifier):

    def __init__(self, sock, account_name):
        self.sock = sock
        self.account_name = account_name
        super().__init__()

    # перегружаем ран от тредов
    def run(self):
        while True:
            try:
                message = get_message(self.sock)
                # проверяем кому отправлено сообщение
                if 'action' in message and message['action'] == 'message' and \
                        'sender' in message and 'destination' in message \
                        and 'message_text' in message and message['destination'] == self.account_name:
                    session = create_session()
                    logger.info(f'{message["sender"]}: {message["message_text"]}')
                    new_mes_history = MessageHistory(from_user_name=message["sender"],
                                                     to_user_name=message['destination'],
                                                     message=message["message_text"],
                                                     date=datetime.now())
                    session.add(new_mes_history)
                    session.commit()
                    session.close()
                elif 'response' in message and 'alert' in message:
                    print('Обнаружены пользователи:')
                    for i in message['alert']:
                        print(i)
                else:
                    logger.error(f'Получено некорректное сообщение от сервера: {message}')
            except (OSError, ConnectionError, ConnectionAbortedError,
                    ConnectionResetError, json.JSONDecodeError):
                logger.critical(f'Потеряно соединение с сервером.')
                break


def main():
    """
    В командной строке запустить: py client.py <host> <int:port>.
    """
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            logger.error('Порт должен быть в диапазоне от 1024 до 65535.')
            raise ValueError
    except IndexError:
        logger.debug('Применяются дефолтные настройки хоста и порта')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        sys.exit(1)

    client_name = input('Введите имя пользователя: ')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_address, server_port))

    message_to_server = create_presence(client_name)
    send_message(client, message_to_server, ENCODING)
    try:
        answer = process_ans(get_message(client, MAX_PACKAGE_LENGTH, ENCODING))
        logger.debug(answer)
    except Exception as e:
        logger.error('Не удалось декодировать сообщение сервера.')
    else:

        # поток приёма сообщений
        receiver = ClientReceiver(client, client_name)
        receiver.daemon = True
        receiver.start()

        # затем запускаем отправку сообщений и взаимодействие с пользователем.
        user_interface = ClientSender(client_name, client)
        user_interface.daemon = True
        user_interface.start()
        logger.debug('Запущены оба процесса')

        # если оба потока упали, то завершится выполнение скрипта
        while True:
            time.sleep(1)
            if receiver.is_alive() and user_interface.is_alive():
                continue
            logger.info('Отключение клиентской стороны')
            break


if __name__ == '__main__':
    main()
