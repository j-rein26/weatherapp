import os
from dotenv import load_dotenv
import requests


load_dotenv()
WEATHER_API = os.getenv("WEATHER_API")


def get_data(place, forecast_days=None, type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_API}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if type == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if type == "Weather Conditions":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3,type="Weather Conditions"))
