from todolist import app

@app.route("/hello/")
def hello():
    return "hello world"