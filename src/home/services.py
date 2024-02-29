import requests
from django.conf import settings


def send_message(title: str, message: str) -> None:
    pushover_url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": settings.PUSHOVER_API_TOKEN,
        "user": settings.PUSHOVER_USER_KEY,
        "title": title,
        "message": message,
    }
    response = requests.post(pushover_url, data=data)
    response.raise_for_status()
