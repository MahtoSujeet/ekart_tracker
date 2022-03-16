from dotenv import load_dotenv
import requests
import os
from ekart import Ekart
import json
import time


load_dotenv()
ORDER_ID = "FMPP1104066047"
API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

def send_msg(text, chat_id=-1001576544273):
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}")
        print("msg sent on telegram")


def main():
    ekart = Ekart(api_key=API_KEY)
    last_event = None

    update = None # value will be assigned in while loop
    while True:
        status = ekart.get_status(ORDER_ID)
        data = json.loads(status)
        print(data)

        # update = data.get("data").get("lastEvent")
        try:
            update = data["data"]["lastEvent"]
        except KeyError:
            pass

        print(update)
        if update != last_event:
            last_event = update
            send_msg(text=f"""Update on chess delivery:
{last_event}""")

        time.sleep(15*60)

if __name__ == "__main__":
    main()

