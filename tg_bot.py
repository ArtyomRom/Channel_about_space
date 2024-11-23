import os
import telegram
import requests
from dotenv import load_dotenv

load_dotenv()
def send_photo():
    bot = telegram.Bot(token=os.getenv('TG_BOT_API'))
    url_send_photo = f'https://api.telegram.org/bot{os.getenv("TG_BOT_API")}/sendPhoto'
    data = {'chat_id': '@SpaceX_img'}

    for filename in os.listdir('images'):
        if not filename.endswith('.txt'):
            with open('images/' + filename, 'rb') as image:
                base_name = filename.split('.')[0]
                text_file_path = f'{base_name}_text.txt'
                if text_file_path in os.listdir('images'):
                    with open('images/' + text_file_path, 'r') as text:
                        caption = text.read()
                        data['caption'] = caption
                    os.remove(f'images/{text_file_path}')
                file = {'photo': image}
                requests.post(url_send_photo, files=file, data=data)
            os.remove(f'images/{filename}')

