from tg_bot import send_photos
import time

def public_photo(link: str, tg_bot_api: str, time_public: int):
    while True:
        send_photos(link, tg_bot_api)
        time.sleep(time_public * 3600)