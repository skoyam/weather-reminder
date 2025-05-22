import os
import requests as req

"""
message system which sends an email using mailgun's api
"""


class Notifier:
    def __init__(self):
        # grab api keys/domain/email to send from/target email from.env
        self.api_key = os.getenv("MAILGUN_API_KEY")
        self.domain = os.getenv("MAILGUN_DOMAIN")
        self.from_email = os.getenv("MAILGUN_FROM_EMAIL")
        self.to_email = os.getenv("TARGET_EMAIL")

        # usage for mailgun
        self.base_url = f"https://api.mailgun.net/v3/{self.domain}/messages"

    # sends the message as a str
    def send(self, message: str):
        # dict holding all the data containing where to send from, to, the header, and the message body as described by the example mailgun usage
        data = {
            "from": self.from_email,
            "to": self.to_email,
            "subject": "Weather Reminder",
            "text": message,
        }

        # res
        response = req.post(self.base_url, auth=("api", self.api_key), data=data)

        # 200 is status code OK
        if response.status_code == 200:
            print("Email sent successfully")
        else:
            print(f"Failed to send email: {response.status_code} {response.text}")
