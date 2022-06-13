from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods = ['POST', 'GET'])
@login_required
def home():
    if current_user.correct_guesses >= 1:
        return render_template("tommorow.html", user = current_user)
    else:
        data = request.form
        if request.method == 'POST':
            songGuess = request.form.get('songTitle')
            if songGuess.lower() == "runaway":
                return redirect(url_for('views.correctGuess'))
            else:
                if current_user.attempts_taken == 6:
                    current_user.attempts_taken = 0
                    db.session.commit()
                    return redirect(url_for('views.loseScreen'))
                current_user.attempts_taken += 1
                db.session.commit()
                return redirect(url_for('views.wrongGuess'))
    return render_template('home.html', user = current_user)

@views.route('/wrongGuess')
@login_required
def wrongGuess():
    current_user.attempts_taken += 1
    db.session.commit()
    flash("Incorrect Guess", category = "error")
    return redirect(url_for('views.home'))

@views.route('/correctGuess')
@login_required
def correctGuess():
    attempts_taken = current_user.attempts_taken
    current_user.attempts_taken = 0
    current_user.correct_guesses += 1
    db.session.commit()
    all_users = User.query.all()
    return render_template('correctGuess.html', user= current_user)

@views.route('/loseScreen')
@login_required
def loseScreen():
    return render_template('loseScreen.html', user = current_user)

@views.route('/leaderboard')
def leaderboard():
    all_users = User.query.all()
    return render_template('leaderboard.html', all_users =all_users, user = current_user)
