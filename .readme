# Weather Reminder

Often times in college, I would forget to bring a jacket or umbrella if there was inclement weather. This kinda sucked because my backpack and items would get wet, and it basically ruined my whole day :(

    That's why I created Weather Reminder, a simple email messaging system that assesses the weather
    prior to you waking up and sends you a nice message letting you know how to prepare for the day!

This project was mainly a way for me to leverage learning about API usage in Python and use tools such as WeatherAPI.com for retrieving real-time data about current weather around my location, MailGun for sending an email every morning before my day started to remind myself to bring my umbrella if it was raining or wear a jacket if it was less than 10 degrees Celsius (50 degrees F) outside.

## Features

- **Continuous deployment from Heroku**  
  _To consistently run the program everyday at 9:00AM EST_

- **Analyzes live weather data (via WeatherAPI.com)**  
  _And classifies it as cold or rainy to ensure that you would never be caught unprepared_

- **Sends to a personal email**  
  _With a description stating to wear a jacket or bring an umbrella_

- **Sensitive credentials and settings are managed securely**  
  _Using environment variables, keeping deployment clean and configurable_

- **Mailgun’s reliable email delivery service**  
  _Was utilized for their sandbox support in testing and can be production-ready for verified domains_

- **Modular codebase**  
  _Allows for quick customization_

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

```
WEATHER_API_KEY = openweathermap_api_key
MAILGUN_API_KEY = mailgun_private_api_key
MAILGUN_DOMAIN = mailgun_verified_domain -> make sure this is verified
MAILGUN_FROM_EMAIL = verified_mailgun_sender_email -> again verify through the sender
TARGET_EMAIL = recipient_email_address
LOCATION = city,country_code (ex. Raleigh, Albany)
```
