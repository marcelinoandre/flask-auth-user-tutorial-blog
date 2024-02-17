from flask import Flask, request
from models.user import User
from database import db
from flask_login import LoginManager, login_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "eb5cc3e79b6aaf466637e8c660ca0d28"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.login_view = "login"


@app.route("/")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.run(debug=True)
