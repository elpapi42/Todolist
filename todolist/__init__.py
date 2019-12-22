from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from todolist.api import api_bp
from todolist.web import web_bp

def create_app(mode="development"):
    """ 
    Init core application 

    args:
        mode (str): mode of app creation: "production", "development", "test". dafult="development"
    
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile("{name}.py".format(name=mode))
    app.testing = (mode == "test")

    # Init Plugins
    db.init_app(app)

    with app.app_context():
        app.register_blueprint(web_bp)
        app.register_blueprint(api_bp, url_prefix="/api")

        # Drop all the tables from test database if in test mode
        if(app.testing):
            db.drop_all()
        
        # Create table for models
        db.create_all()

        return app


