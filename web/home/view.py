import os
from distutils.util import strtobool

from flask import Blueprint, render_template
from mcstatus import MinecraftServer
import asyncio

home = Blueprint('home', __name__,
                 template_folder='pages',
                 static_url_path='',
                 static_folder='static')

TIMEOUT = 0.1


@home.route('/')
def index():
    version = 'N/A'
    max_number = 'null'
    current = 'null'
    players = None

    server = MinecraftServer.lookup(os.getenv("MC_SERVER_HOST"))

    new_loop = asyncio.new_event_loop()  # 非主程序無法直接 get_event_loop, 所以 new 一個
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()

    status = request_server_info(loop, server.status)
    if status is not None:
        version = status.version.name
        max_number = status.players.max
        current = status.players.online

    query = request_server_info(loop, server.query)
    if query is not None:
        players = ",".join(query.players.names)

    if strtobool(os.getenv("IS_DEBUG")):
        players = ["Capillary_J,Unidentified"]

    return render_template('main.html',
                           version=version,
                           max_number=max_number,
                           current=current,
                           players=players)


def request_server_info(loop, f):
    response = None
    future = asyncio.wait_for(loop.run_in_executor(None, f), TIMEOUT)
    try:
        response = loop.run_until_complete(future)
    except asyncio.TimeoutError:
        print('MC Server timeout.')
    except ConnectionRefusedError:
        print('MC Server down.')

    return response
