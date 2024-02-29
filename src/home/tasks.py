from dramatiq import actor

from .services import send_message


@actor
def async_send_message(title: str, message: str):
    send_message(title, message)
