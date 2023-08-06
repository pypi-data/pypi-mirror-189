from setuptools import setup, find_packages

setup(
    name='ConnectToSql',
    version='0.1',
    description='A package to simplify the process of connecting to and executing queries on SQL databases',
    author='Sakib',
    author_email='datasec@yopmail.com',
    packages=find_packages(),
    install_requires=['pymysql', 'psycopg2', 'pyodbc']
)
