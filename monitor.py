import requests
import time

BOT_TOKEN = "8577847140:AAGufo6iYE4jMacG0O7LOML7bbPOQlUcu_c"
CHAT_ID = "851468594"

URL = "https://shop.royalchallengers.com"  # change if needed

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_tickets():
    try:
        res = requests.get(URL)
        text = res.text.lower()

        if "sold out" not in text:
            send_telegram("🚨 RCB Tickets might be LIVE! Check now 👉 " + URL)
        else:
            print("No tickets yet")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    check_tickets()
