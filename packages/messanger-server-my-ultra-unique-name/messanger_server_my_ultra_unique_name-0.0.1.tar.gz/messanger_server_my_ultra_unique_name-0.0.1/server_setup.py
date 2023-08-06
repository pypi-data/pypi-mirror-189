from setuptools import setup, find_packages

setup(name="messanger_server_my_ultra_unique_name",
      version="0.0.1",
      description="server_side_of_messanger",
      author="Maxim",
      author_email="",
      packages=find_packages(),
      install_requires=['PyQt5', 'tabulate', 'sqlalchemy', 'sphinx', 'wheel', 'cx-Freeze']
      )
