from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Register, Login


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "changethisfuckingstring"  # Change this


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


@app.route('/signup', methods=['GET', 'POST'])
def signupPage():
    form = Register()
    username = form.username.data

    if form.validate_on_submit():
        print(form.password.errors)
        flash(f"New account for {username} created successfully !", 'success')
        return redirect(url_for('loginPage'))

    return render_template('signup.html', form=form)


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


# @app.route('/api/auth/signup', methods=['POST'])
# def signupApi():
#     data = request.form
#     username = data.get('username')
#     password = data.get('password')
#     name = data.get('name')

#     exist = User.query.filter(User.username.in_([username])).first()

#     if exist != None:
#         return "USER EXISTS"
#     else:

        # newUser = User(username=username, password=password, name=name)
        # db.session.add(newUser)
        # db.session.commit()
        # return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
