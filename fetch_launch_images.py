from common import download_photo
import requests


def get_images_from_launch(params: dict, id=None):
    if not id:
        response = requests.get('https://api.spacexdata.com/v5/launches')
    else:
        parameters = {'id': id}
        response = requests.get('https://api.spacexdata.com/v5/launches/', params=parameters)
    response.raise_for_status()
    launches = response.json()
    count = 0
    for launche in launches:
        for index, photo in enumerate(launche['links']['flickr']['original']):
            download_photo(photo, f'images/spacex_{count}.jpeg', params)
            count += 1
            if launche['details']:
                with open(f'images/spacex_{count}_text.txt', 'w', encoding='utf-8') as file:
                    file.write(launche['details'])
