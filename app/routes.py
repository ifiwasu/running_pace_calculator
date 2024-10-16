from flask import Blueprint, render_template, redirect, url_for
from app.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # logica voor route hier plaatsen en pass weghalen
        pass
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic for handling login, like checking credentials
        # After successful login, redirect to the home page
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

