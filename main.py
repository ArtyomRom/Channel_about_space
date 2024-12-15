from fetch_launch_images import get_images_from_launch
from fetch_earth_images import get_images_of_the_earth
from fetch_nasa_images import get_images_from_nasa
from dotenv import load_dotenv
import pathlib
import argparse
import os


def main():
    load_dotenv()
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачать фотографии земли, старты ракет или космоса'
    )
    parser.add_argument('--launch_id', default=None,
                        help='Введите ID старта, если такой присутствует')
    parser.add_argument('--nasa', default=False,
                        help='Получить фотографии от Nasa')
    parser.add_argument('--launch', default=False,
                        help='Получить фотографии со старта')
    parser.add_argument('--earth', default=False,
                        help='Получить фотографии планеты')

    args = parser.parse_args()
    parser.print_help()
    launch_id = args.launch_id
    nasa = args.nasa
    launch = args.launch
    earth = args.earth
    params = {'api_key': os.getenv('NASA_API_KEY')}
    if nasa:
        get_images_from_nasa(params)
    if launch:
        get_images_from_launch(params, launch_id)
    if earth:
        get_images_of_the_earth(params)


if __name__ == '__main__':
    main()
