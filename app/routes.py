from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from flask import render_template, request, redirect, flash, url_for
from app.forms import Register, Login
from app import app, db, bcrypt


@app.route('/', methods=['GET', 'POST'])
def loginPage():
    if current_user.is_authenticated:
        return redirect(url_for('userProfile'))
    form = Login()

    if form.validate_on_submit():  # on submit
        # check if username exist
        user = User.query.filter_by(username=form.username.data).first()

        # check if username and password matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)  # then log in
            return redirect(url_for('userProfile'))  # redirect to profile page

        else:
            flash('Incorrect Username or Password', 'danger')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signupPage():
    if current_user.is_authenticated:
        return redirect(url_for('userProfile'))
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


@app.route('/logout')
def logOut():
    logout_user()
    flash('Logged out!', 'success')
    return redirect(url_for('loginPage'))


@app.route('/profile')
@login_required
def userProfile():
    avatar_pic = f"https://avatars.dicebear.com/api/micah/{current_user.name}.svg"
    return render_template('profile.html', avatar_pic=avatar_pic)
