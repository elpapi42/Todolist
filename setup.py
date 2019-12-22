from setuptools import setup, find_packages

setup(
    name='todolist',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'validator_collection'
    ],
)