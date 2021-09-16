from re import U
from app.models import User
from flask import render_template, request, redirect, flash, url_for
from app.forms import Register, Login
from app import app, db, bcrypt


@app.route('/', methods=['GET', 'POST'])
def loginPage():
    form = Login()

    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':

            # Returns a flashed message
            flash('Logged in successfully', 'success')
            return redirect(url_for('/profile'))
        else:
            flash('Incorrect Username or Password', 'danger')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signupPage():
    form = Register()
    username = form.username.data

    if form.validate_on_submit():

        # ------- hashes the pass for security---
        hashed = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # ---------------------------------------

        # ---------Create user-----------
        user = User(name=form.name.data,
                    username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        # --------------------------------

        flash(
            f"New account for {username} has been created! Please login..", 'success')
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
