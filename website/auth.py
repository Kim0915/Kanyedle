from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        submitted_username = request.form.get('username')

        user = User.query.filter_by(username = submitted_username).first()
         
        if not user:
            new_user = User(username = submitted_username, correct_guesses = 0, attempts_taken = 0)
            db.session.add(new_user)
            db.session.commit()
        user = User.query.filter_by(username = submitted_username).first()
        login_user(user, remember=True)
        return redirect(url_for("views.home"))
    return render_template("login.html", user = current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
