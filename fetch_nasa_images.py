import pprint

from common import get_the_file_extension, fetch_spacex_last_launch
from dotenv import load_dotenv
import requests
import os


load_dotenv()
def getting_images_from_nasa():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': os.getenv('NASA_API_KEY'), 'count': 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for image in response.json():
        try:
            file_name = get_the_file_extension(image['hdurl'])
            fetch_spacex_last_launch(image['url'], f'images/nasa_{file_name}')
            base_name = file_name.split('.')[0]
            text_file_path = f'{base_name}_text.txt'
            with open(f'images/nasa_{text_file_path}', 'w', encoding='utf-8') as text:
                text.write(image['explanation'])
        except KeyError:
            continue

