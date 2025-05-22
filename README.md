<p align="center">
  <img src="https://github.com/skoyam/weather-reminder/blob/main/docs/logo.png?raw=true" alt="Logo" width="300"/>
</p>


# Motivation

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

## Example Usage (with Heroku Deployment)

Simply running this project from the command line, it would output this:

<p align="center">
  <img src="https://github.com/user-attachments/assets/c9847a1e-2215-4742-9bf2-8150fe06e19a" alt="CLI Output" width="400"/>
</p>

What Heroku does is that it has a job, which runs this line of code everyday at 06:00AM UTC (9:00AM EST), and that's the continous deployment aspect of this app. Replication would include creating a new job in Heroku with these specifications.

<p align="center">
  <img src="https://github.com/skoyam/weather-reminder/blob/main/docs/heroku.png?raw=true" alt="CLI Output" width="800"/>
</p>

After the weather has been parsed, an email will be sent if there is inclement weather predicted for the day as shown below:

<p align="center">
  <img src="https://github.com/skoyam/weather-reminder/blob/main/docs/email.png?raw=true" alt="CLI Output" width="600"/>
</p>




