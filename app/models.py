from app import db
from app import login_manager
# is auth, is anonymous, is alive session thingies
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)

    username = db.Column(db.String(20), unique=True,
                         nullable=False)  # maximum 8 characters

    password = db.Column(db.String, nullable=False)

    profile_pic = db.Column(db.String, nullable=False, default='profile.png')

    def __repr__(self):
        return f"Name: {self.name} Username: {self.username}"
