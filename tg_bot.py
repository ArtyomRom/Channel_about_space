import os
import requests

def send_photo(link_tg_channel, tg_bot_api):
    url_send_photo = f'https://api.telegram.org/bot{tg_bot_api}/sendPhoto'
    data = {'chat_id': link_tg_channel}

    for filename in os.listdir('images'):
        if not filename.endswith('.txt'):
            with open(f'images/{filename}', 'rb') as image:
                data['caption'] = send_text(filename)
                file = {'photo': image}
                requests.post(url_send_photo, files=file, data=data)
        break

def send_text(filename):
    base_name = filename.split('.')[0]
    text_file_path = f'{base_name}_text.txt'
    if text_file_path in os.listdir('images'):
        with open(f'images/{text_file_path}', 'r') as text:
            caption = text.read()
            return caption
