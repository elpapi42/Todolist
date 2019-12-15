from setuptools import setup

setup(
    name='todolist',
    packages=['todolist'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)