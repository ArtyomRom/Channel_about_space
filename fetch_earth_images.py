from common import download_photo
import requests


def get_images_of_the_earth(params):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    for image_earth in response.json():
        date = image_earth['date'].split()[0].replace('-', '/')
        image = image_earth['image']
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        download_photo(url, f'images/earth_{image}.jpeg', params)
