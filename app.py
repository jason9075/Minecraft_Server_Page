import glob
import os
import platform
import shutil
import time

from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='static')


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
