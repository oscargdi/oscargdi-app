from dramatiq import actor
from dramatiq_crontab import cron

from .services import send_message


@actor(queue_name="send_message")
def async_send_message(title: str, message: str):
    send_message(title, message)


@cron("*/5 * * * *")
@actor(queue_name="send_message_scheduled")
def async_send_message_scheduled():
    send_message(
        "Scheduled message", "This message was scheduled to be sent every 5 minutes."
    )
