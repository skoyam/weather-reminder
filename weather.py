import requests as req


"""
fetches weather data from the api key and location given after parsing the resulting json from the request
"""


class WeatherFetcher:
    """grab api key and location"""

    def __init__(self, api_key: str, location: str):
        self.api_key = api_key
        self.location = location

    """ scrape weather data from url """

    def get_weather(self) -> dict:
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={self.location}"

        # get the response from the url and turn it into a json to parse
        response = req.get(url)
        response.raise_for_status()
        scraped_weather_data = response.json()

        # temp data from the pretty print
        temp = scraped_weather_data["current"]["temp_c"]
        # add the [0] since theres another list inside containing the desc
        weather_desc = scraped_weather_data["current"]["condition"]["text"].lower()

        # if we find rain in the weahter or the temp lower than 50 deg F, its cold chief
        is_rainy = "rain" in weather_desc
        is_cold = temp < 10  # centigrade

        # return a dict object containing all this data
        return {
            "temp": temp,
            "description": weather_desc,
            "is_rainy": is_rainy,
            "is_cold": is_cold,
        }
