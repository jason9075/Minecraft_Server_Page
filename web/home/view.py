from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='pages', static_folder='static')


@home.route('/')
@home.route('/home')
def index():
    return render_template('main.html')
