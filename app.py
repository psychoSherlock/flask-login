from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(8), unique=True,
                         nullable=False)  # maximum 8 characters
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Name: {self.name} Username: {self.username}"


@app.route('/')
def loginPage():
    return render_template('login.html')


@app.route('/signup')
def signupPage():
    return render_template('signup.html')


@app.route('/api/auth/login', methods=['POST'])
def loginApi():
    data = request.form

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter(User.username.in_(
        [username]), User.password.in_([password])).first()

    if user:
        return user.name
    else:
        return 'Not Found'


@app.route('/api/auth/signup', methods=['POST'])
def signupApi():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')

    exist = User.query.filter(User.username.in_([username])).first()

    if exist != None:
        return "USER EXISTS"
    else:

        newUser = User(username=username, password=password, name=name)
        db.session.add(newUser)
        db.session.commit()
        return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500, debug=True)
