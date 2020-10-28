import os
from distutils.util import strtobool

from flask import Blueprint, render_template
from mcstatus import MinecraftServer

home = Blueprint('home', __name__,
                 template_folder='pages',
                 static_url_path='',
                 static_folder='static')


@home.route('/')
def index():
    server = MinecraftServer.lookup(os.getenv("MC_SERVER_HOST"))
    status = server.status()
    players = ""
    if strtobool(os.getenv("ENABLE_QUERY")):
        query = server.query()
        players = "\n".join(query.players.names)
    return render_template('main.html',
                           version=status.version.name,
                           max_number=status.players.max,
                           current=status.players.online,
                           players=players)
