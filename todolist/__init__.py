import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import api_bp
from web import web_bp

db = SQLAlchemy()

def create_app():
    """ Init core application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile("config.py")

    # Init Plugins
    db.init_app(app)

    with app.app_context():
        app.register_blueprint(web_bp)
        app.register_blueprint(api_bp, url_prefix="/api")
        
        #Create table for models
        db.create_all()

        return app


