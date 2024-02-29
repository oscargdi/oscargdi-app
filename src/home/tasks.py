from dramatiq import actor

from .services import send_message


@actor(queue_name="send_message")
def async_send_message(title: str, message: str):
    send_message(title, message)
