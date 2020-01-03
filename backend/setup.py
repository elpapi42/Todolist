import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

INSTALL_REQUIRES = [
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
]

TEST_REQUIRES = [
    'pytest',
    'psycopg2-binary'
]

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        subprocess.check_call([sys.executable, "-m", "pip", "install", *TEST_REQUIRES])
        develop.run(self)

setup(
    author="Whitman Bohorquez, Jorge Ocaris, Jesus Perez",
    author_email="whitman-2@hotmail.com",
    name='todolist',
    license="MIT",
    description='Backend Server for a Todolist-Like Application',
    version='1.0.0',
    url='https://github.com/ElPapi42/Todolist',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
    ],
    cmdclass={
        'develop': PostDevelopCommand,
    },
)








