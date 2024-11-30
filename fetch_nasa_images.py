from common import get_the_file_extension, download_photo
from contextlib import suppress
import requests


def get_images_from_nasa(params: dict):
    url = 'https://api.nasa.gov/planetary/apod'
    parameters = params.copy()
    parameters['count'] = 30
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    for image in response.json():
        with suppress(KeyError):
            file_name = get_the_file_extension(image['hdurl'])
            download_photo(image['url'], f'images/nasa_{file_name}', params)
            base_name = file_name.split('.')[0]
            text_file_path = f'{base_name}_text.txt'
            with open(f'images/nasa_{text_file_path}', 'w', encoding='utf-8') as text:
                text.write(image['explanation'])