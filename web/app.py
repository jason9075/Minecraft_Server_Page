from flask import Flask

from web.home.view import home
from web.overviewer.view import ov

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(ov, url_prefix='/overviewer')

print(app.url_map)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
