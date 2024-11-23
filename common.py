from urllib.parse import urlparse
from dotenv import load_dotenv
import urllib
import requests
import os

load_dotenv()

def fetch_spacex_last_launch(url: str, path: str):
    params = {'api_key': os.getenv('NASA_API_KEY')}
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_the_file_extension(url: str) -> str:
    parsed_url = urlparse(url)
    file_name = parsed_url.path.split('/')[-1]
    return urllib.parse.unquote(file_name)