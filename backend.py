import os
from dotenv import load_dotenv
import requests


load_dotenv()
WEATHER_API = os.getenv("WEATHER_API")

def get_data(place, forecast_days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_API}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))
