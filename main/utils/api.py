import requests
import json

API_KEY = '4fb58853c7917f3aa844a78cd28a80aa'
def get_weather_by_coordinates(lat, lon, exclude, units):
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': exclude,
        'units': units,
        'appid': API_KEY
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

    try:
        data = response.json()
        return json.dumps(data, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)

weather_data = get_weather_by_coordinates(53.2194, 63.6354, 'current', 'metric')
print(weather_data)