from django.conf import settings
from pysendpulse.pysendpulse import PySendPulse


def _get_SPApiProxy():
    return PySendPulse(settings.SEND_PULSE_API_ID,
                       settings.SEND_PULSE_API_SECRET,
                       settings.SEND_PULSE_TOKEN_STORAGE,
                      )

def add_subscriber_to_sendpulse(subscriber):
    subscriber_for_add = [
        {
            'email': subscriber.email,
            'variables': {
                'Имя': subscriber.name,
            }
        }
    ]
    SPApiProxy = _get_SPApiProxy()
    addition_result = SPApiProxy.add_emails_to_addressbook(
                            settings.SEND_PULSE_API_SUBSCRIBER_BOOK_ID, 
                            subscriber_for_add,
                            )
    return addition_result