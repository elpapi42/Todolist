from setuptools import setup, find_packages

setup(
    name='todolist',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask>=0.10.1',
        'flask-restful',
        'flask-sqlalchemy',
        'validator_collection',
        'python-dotenv',
        'psycopg2'
    ],
)