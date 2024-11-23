from common import fetch_spacex_last_launch
from dotenv import load_dotenv
import requests
import os



load_dotenv()
def getting_images_of_the_earth():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': os.getenv('NASA_API_KEY')}
    response = requests.get(url, params=params)
    response.raise_for_status()
    count = 0
    for image_earth in response.json():
        date = image_earth['date'].split()[0].replace('-', '/')
        image = image_earth['image']
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        fetch_spacex_last_launch(url, f'images/earth_{image}.jpeg')
        count += 1
        if count == 5:
            break
