import requests
import json

API_KEY = '4fb58853c7917f3aa844a78cd28a80aa'

class Weather_API:
    def __init__(self, temp, weather, wind_speed, humidity, header):
        self.temp = temp
        self.weather = weather
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.header = header

    @staticmethod
    def get_weather_data(lat, lon, units='metric', index=0):
        params = {
            'lat': lat,
            'lon': lon,
            'units': units,
            'appid': API_KEY
        }

        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            weather_data = {
                'temp': round(data['list'][index]['main']['temp']),
                'weather': data['list'][index]['weather'][0]['main'],
                'wind_speed': data['list'][index]['wind']['speed'],
                'humidity': data['list'][index]['main']['humidity'],
            }

            return weather_data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from OpenWeatherMap: {e}")
            return None

    @staticmethod
    def get_city_weather_data(city, header, index=0, units='metric'):
        params = {
            'q': city,
            'units': units,
            'appid': API_KEY
        }

        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data['message'] == 0:
                pass
            else:
                return 'City not found'

            weather_data = {
                'temp': round(data['list'][index]['main']['temp']),
                'weather': data['list'][index]['weather'][0]['main'],
                'wind_speed': data['list'][index]['wind']['speed'],
                'humidity': data['list'][index]['main']['humidity'],
                'header': header,
            }

            return weather_data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from OpenWeatherMap: {e}")
            return None

    def __str__(self):
        return f'Temperature: {self.temp}°C, Weather: {self.weather}, Wind Speed: {self.wind_speed} m/s, Humidity: {self.humidity}%, Header: {self.header}'

