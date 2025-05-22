from dotenv import load_dotenv
import os
from weather import WeatherFetcher
from notifier import Notifier

"""
creates the reminder bot used to get the weather from OpenWeatherMap, and notifier from Twilio

- sends a message to the user with a weather description and classifies to see whether its cold or rainy
- if neither, we don't send a notif since its not needed, we can modify it to send a happy message but for my intents + purposes just an important notif is fine
"""


class ReminderBot:
    """initializes the weather and notif"""

    def __init__(self, weather_fetcher, notifier):
        self.weather = weather_fetcher
        self.notifier = notifier

    """ runs the application """

    def run(self):
        # get the curr weather
        data = self.weather.get_weather()
        print(f"Current Weather: {data['description']} | {data['temp']}°C")

        message = "good morning!!"
        if data["rain"]:
            message += "get an umbrella bro its rainy"
        if data["cold"]:
            message += "brrrr wear a jacket its cold"

        # after appending the msg, we can ping the phone
        if data["is_rainy"] or data["is_cold"]:
            # send the ping to the user
            self.notifier.send(message)
            print("notif sent")
        else:
            print("nah ur good bro")


# if running from cli here
if __name__ == "__main__":
    load_dotenv()
    wf = WeatherFetcher(
        os.getenv("WEATHER_API_KEY"), os.getenv("LOCATION", "Raleigh,NC")
    )
    nt = Notifier()
    bot = ReminderBot(wf, nt)
    bot.run()
