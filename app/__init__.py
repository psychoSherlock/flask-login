

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "changethisfuckingstring"  # Change this

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginPage'
login_manager.login_message_category = "warning"
from app import routes