import requests
import time
import random

# RECOMMENDED: Use Environment Variables for these instead of hardcoding!
BOT_TOKEN = "8577847140:AAGufo6iYE4jMacG0O7LOML7bbPOQlUcu_c"
CHAT_ID = "851468594"
URL = "https://shop.royalchallengers.com"

def send_telegram(msg):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(api_url, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except Exception as e:
        print(f"Failed to send Telegram: {e}")

def check_tickets():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    cache_buster = f"{URL}?v={random.randint(1, 100000)}"

    try:
        res = requests.get(cache_buster, headers=headers, timeout=15)
        res.raise_for_status() # Check if the site is actually up (200 OK)
        
        text = res.text.lower()

        if "buy" in text or "book" in text or "available" in text:
            send_telegram(f"🚨 TICKETS MIGHT BE LIVE! \nCheck now: {URL}")
            print("Alert sent!")
        else:
            print("Still sold out / No tickets found.")

    except Exception as e:
        print(f"Error checking site: {e}")

if __name__ == "__main__":
    check_tickets()
