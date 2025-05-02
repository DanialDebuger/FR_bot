import requests

BOT_TOKEN = "7450144082:AAE01axIqp8yUZ4xX2BxGJTOqGKGfe9KKjw"
AUTHORIZED_CHAT_ID = 5660835662  # عددی جایگزین شود

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": AUTHORIZED_CHAT_ID, "text": message}
    requests.post(url, data=payload)