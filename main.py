from fetch_launch_images import get_images_from_launch
from fetch_earth_images import get_images_of_the_earth
from fetch_nasa_images import get_images_from_nasa
from tg_bot import send_photo
from dotenv import load_dotenv
import pathlib
import argparse
import time
import os


def main():
    load_dotenv()
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачать фотографии земли, старты ракет или космоса'
    )
    parser.add_argument('--id', default=False,
                        help='Введите ID старта, если такой присутствует')
    parser.add_argument('--nasa', default=False,
                        help='Получить фотографии от Nasa')
    parser.add_argument('--launch', default=False,
                        help='Получить фотографии со старта')
    parser.add_argument('--earth', default=False,
                        help='Получить фотографии планеты')
    parser.add_argument('--time_public', default=4,
                        help='Указать промежуток времения публикаций фотографий')
    parser.add_argument('--public', default=0,
                        help='Публиковать посты в телеграмм канал')
    args = parser.parse_args()
    parser.print_help()
    id = args.id
    nasa = args.nasa
    launch = args.launch
    earth = args.earth
    time_public = args.time_public
    public = args.public
    params = {'api_key': os.getenv('NASA_API_KEY')}
    if nasa:
        get_images_from_nasa(params)
    if launch:
        get_images_from_launch(params, id)
    if earth:
        get_images_of_the_earth(params)

    while public:
        send_photo(os.getenv('link_tg_channel'), os.getenv('TG_BOT_API'))
        time.sleep(time_public * 3600)


if __name__ == '__main__':
    main()
