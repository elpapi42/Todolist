import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "7hy5680955/7.2;as6sa324156dsfgh2548sdwbe8d8d8d0f978559f9595g99d7s6a4422"

    DB_NAME = "todolist"#os.environ["DB_NAME"]
    DB_USERNAME = "postgres"#os.environ["DB_USERNAME"]
    DB_PASSWORD = "root"#os.environ["DB_PASSWORD"]

    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/todolist"#os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = True