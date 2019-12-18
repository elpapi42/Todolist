from flask_migrate import Migrate
from todolist import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


