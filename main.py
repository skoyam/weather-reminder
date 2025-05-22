from dotenv import load_dotenv
import os
from weather import WeatherFetcher
from notifier import Notifier

"""
creates the reminder bot used to get the weather from OpenWeatherMap, and notifier from Twilio

- sends a message to the user with a weather description and classifies to see whether its cold or rainy
- if neither, we don't send a notif since its not needed, we can modify it to send a happy message but for my intents + purposes just an important notif is fine
"""

# was testing grabbing the api key
# load_dotenv()
# print(f"WEATHER_API_KEY = '{os.getenv('WEATHER_API_KEY')}'")


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

        message = "good morning!! 🌞\n"

        if data["is_rainy"]:
            message += "☔ don't forget your umbrella — it's rainy out!\n"
        if data["is_cold"]:
            message += "🧥 brrrr... wear a jacket, it's cold today!\n"

        print(message)

        # after appending the msg, we can ping the phone
        if data["is_rainy"] or data["is_cold"]:
            # send the ping to the user
            self.notifier.send(message)
            print("notif sent")
        else:
            print("nah ur good bro")


# if running from cli here
if __name__ == "__main__":
    # grab from .env
    load_dotenv()
    # setup wf using api key and location of shelton
    wf = WeatherFetcher(os.getenv("WEATHER_API_KEY"), os.getenv("LOCATION", "Shelton"))
    # notifier running
    nt = Notifier()
    # reminder bot encapsulates both with the wf and nt
    bot = ReminderBot(wf, nt)
    # run the bot
    bot.run()
