import os
import socket
from argparse import ArgumentParser

import requests
from dotenv import load_dotenv

parser = ArgumentParser()
parser.add_argument("message", help="message to discord channel.")

load_dotenv()
BOT_NAME = 'Minecraft 小幫手'
DISCORD_AVATAR_URL = 'https://i.imgur.com/2VZywQH.png'


def main():
    args = parser.parse_args()

    url = os.getenv("DISCORD_API")
    assign_ip = os.getenv("ASSIGN_LOCAL_IP")

    my_ip = socket.gethostbyname(socket.gethostname())
    if my_ip != assign_ip:
        print('Not a assign ip, exit program.')
        exit(0)

    message = args.message

    payload = f'username={BOT_NAME}&avatar_url={DISCORD_AVATAR_URL}&content={message}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


if __name__ == '__main__':
    main()
