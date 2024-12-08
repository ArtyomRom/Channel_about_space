from tg_bot import send_photos
from dotenv import load_dotenv
import argparse
import time
import os

def public_photos():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Публикация фото в телеграмм канал'
    )
    parser.add_argument('--time_public', default=4,
                        help='Введите время публикации')
    args = parser.parse_args()
    time_public = args.time_public
    link = os.getenv('link_tg_channel')
    tg_bot_api = os.getenv('tg_bot_api')
    time_public = int(time_public)
    while True:
        send_photos(link, tg_bot_api)
        time.sleep(time_public * 3600)


if __name__ == '__main__':
    public_photos()