import dis


class ServerVerifier(type):

    def __init__(self, cls_name, bases, cls_dict):
        methods = []
        attrs = []
        for func in cls_dict:
            try:
                res = dis.get_instructions(cls_dict[func])
            except TypeError:
                pass
            else:
                for i in res:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attrs:
                            attrs.append(i.argval)
        if 'connect' in methods:
            raise TypeError('Использование метода connect недопустимо в классе сервера')
        super().__init__(cls_name, bases, cls_dict)


class ClientVerifier(type):
    def __init__(self, cls_name, bases, cls_dict):
        methods = []
        for func in cls_dict:
            try:
                res = dis.get_instructions(cls_dict[func])
            except TypeError:
                pass
            else:
                for i in res:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        for func in ('accept', 'listen', 'socket'):
            if func in methods:
                raise TypeError("В классе недопустимо использовать методы 'accept', 'listen', 'socket'")

        super().__init__(cls_name, bases, cls_dict)
