from twilio.rest import Client
import os

"""
sets up the notifier from Twilio and the phone to ping to, as well as the message construction format
"""


class Notifier:
    """get phone and client data"""

    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
        self.from_num = os.getenv("TWILIO_PHONE")
        self.to_num = os.getenv("TARGET_PHONE")

    """message body from twilio number to client phone"""

    def send(self, message: str):
        self.client.messages.create(body=message, from_=self.from_num, to=self.to_num)
