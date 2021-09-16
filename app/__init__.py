from flask_bcrypt import Bcrypt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "changethisfuckingstring"  # Change this

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
from app import routes