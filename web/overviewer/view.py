from flask import Blueprint, render_template

ov = Blueprint('ov', __name__, template_folder='pages',
               static_url_path='',
               static_folder='pages')


@ov.route('/')
def index():
    return render_template('index.html')
