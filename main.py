from fetch_launch_images import getting_images_from_launch
from fetch_earth_images import getting_images_of_the_earth
from fetch_nasa_images import getting_images_from_nasa
from tg_bot import send_photo
import pathlib
import argparse

def main():
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачать фотографии земли, старты ракет или космоса'
    )
    parser.add_argument('--ID', default=False, help='Введите ID старта, если такой присутствует')
    parser.add_argument('--NASA', default=False, help='Получить фотографии от Nasa')
    parser.add_argument('--LAUNCH', default=False, help='Получить фотографии со старта')
    parser.add_argument('--EARTH', default=False, help='Получить фотографии планеты')
    args = parser.parse_args()
    parser.print_help()
    ID = args.ID
    NASA = args.NASA
    LAUNCH = args.LAUNCH
    EARTH = args.EARTH
    if NASA:
        getting_images_from_nasa()
    if LAUNCH:
        getting_images_from_launch(ID)
    if EARTH:
        getting_images_of_the_earth()
    send_photo()

if __name__ == '__main__':
    main()
