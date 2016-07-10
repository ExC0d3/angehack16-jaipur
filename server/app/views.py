from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from app import app, lm
from .forms import LoginForm
from .user import User


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one(
            {"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile():
    return render_template('profile_edit.html')


@app.route('/profile/mariah', methods=['GET', 'POST'])
# @login_required
def mariah():
    return render_template('mariah.html')


@app.route('/profile/sarah', methods=['GET', 'POST'])
# @login_required
def sarah():
    return render_template('sarah.html')


@app.route('/profile/ben', methods=['GET', 'POST'])
# @login_required
def ben():
    return render_template('ben.html')


@app.route('/campaign', methods=['GET', 'POST'])
@login_required
def campaign():
    return render_template('campaigns.html')


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
