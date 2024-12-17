from tg_bot import send_photos
from config import get_env
import argparse
import time


def public_photos(link, tg_bot_api):
    parser = argparse.ArgumentParser(
        description='Публикация фото в телеграмм канал'
    )
    parser.add_argument('--time_public', default=4,
                        help='Введите время публикации')
    args = parser.parse_args()
    time_public = args.time_public
    time_public = int(time_public)
    while True:
        send_photos(link, tg_bot_api)
        time.sleep(time_public * 3600)


if __name__ == '__main__':
    link = get_env('link_tg_channel')
    tg_bot_api = get_env('TG_BOT_API')
    public_photos(link, tg_bot_api)