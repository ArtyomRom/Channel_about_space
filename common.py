from urllib.parse import urlparse
import urllib
import requests


def download_photo(url: str, path: str, params: dict) -> None:
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_the_file_extension(url: str) -> str:
    parsed_url = urlparse(url)
    file_name = parsed_url.path.split('/')[-1]
    return urllib.parse.unquote(file_name)