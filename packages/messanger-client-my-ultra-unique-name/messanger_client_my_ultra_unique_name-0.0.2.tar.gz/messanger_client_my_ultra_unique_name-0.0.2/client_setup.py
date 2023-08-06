from setuptools import setup, find_packages

setup(name="messanger_client_my_ultra_unique_name",
      version="0.0.2",
      description="client_side_of_messanger",
      author="Maxim",
      author_email="",
      packages=find_packages(),
      install_requires=['PyQt5', 'tabulate', 'sqlalchemy', 'sphinx', 'wheel', 'cx-Freeze']
      )
