import requests

API_KEY = "cac3107196187f3d5620f6a16ac282a2"
LOCATION = "Raleigh,NC"

url = f"https://api.openweathermap.org/data/2.5/weather?q={LOCATION}&units=metric&appid={API_KEY}"

response = requests.get(url)
print("Status code:", response.status_code)
print("Response:", response.text)
