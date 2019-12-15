from todolist import app

@app.route("/hello/")
def hello():
    return app.config["DB_NAME"]