from setuptools import setup, find_packages

setup(
    name='todolist',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask>=0.10.1',
        'flask-restful',
        'flask-sqlalchemy',
        'flask-dance',
        'flask-login',
        'validator_collection',
        'python-dotenv',
        'sqlalchemy',
        'sqlalchemy-utils',
        'blinker',
        'pyjwt',
    ],
)