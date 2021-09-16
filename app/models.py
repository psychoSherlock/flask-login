from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)

    username = db.Column(db.String(20), unique=True,
                         nullable=False)  # maximum 8 characters

    password = db.Column(db.String, nullable=False)

    profile_pic = db.Column(db.String, nullable=False, default='profile.png')

    def __repr__(self):
        return f"Name: {self.name} Username: {self.username}"
