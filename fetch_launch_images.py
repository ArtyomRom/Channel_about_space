from common import fetch_spacex_last_launch
from dotenv import load_dotenv
import requests


load_dotenv()

def getting_images_from_launch(id=None):
    if not id:
        response = requests.get(f'https://api.spacexdata.com/v5/launches')
    else:
        params = {'id': id}
        response = requests.get(f'https://api.spacexdata.com/v5/launches/', params=params)
    response.raise_for_status()
    launches = response.json()
    count = 0
    for launche in launches:
        try:
            if launche['links']['flickr']['original']:
                for index, photo in enumerate(launche['links']['flickr']['original']):
                    fetch_spacex_last_launch(photo, f'images/spacex_{count}.jpeg')
                    count += 1
                    if launche['details']:
                        with open(f'images/spacex_{count}_text.txt', 'w') as file:
                            file.write(launche['details'])
                        break
        except:
            continue

