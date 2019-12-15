from flask import Flask

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("todolist.config.ProductionConfig")
else:
    app.config.from_object("todolist.config.DevelopmentConfig")

import todolist.views

