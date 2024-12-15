import os
import requests

def send_photos(link_tg_channel, tg_bot_api):
    photo_url = f'https://api.telegram.org/bot{tg_bot_api}/sendPhoto'
    data = {'chat_id': link_tg_channel}

    for filename in os.listdir('images'):
        if not filename.endswith('.txt'):
            with open(f'images/{filename}', 'rb') as image:
                data['caption'] = get_text(filename)
                file = {'photo': image}
                requests.post(photo_url, files=file, data=data)


def get_text(filename):
    base_name = filename.split('.')[0]
    text_file_path = f'{base_name}_text.txt'
    if text_file_path in os.listdir('images'):
        with open(f'images/{text_file_path}', 'r') as text:
            caption = text.read()
            return caption
