import os

DEBUG = False
TESTING = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_URI")

SESSION_COOKIE_SECURE = True

        
