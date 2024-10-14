from datetime import timedelta
from .weather_api import Weather_API

class APIClient():

    def get_today_data(city, current_time):
            first_data = Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.hour}:00')
            second_data = Weather_API.get_city_weather_data(city, index=1, header=f'{(current_time.hour + 3) % 24}:00')
            third_data = Weather_API.get_city_weather_data(city, index=2, header=f'{(current_time.hour + 6) % 24}:00')
            return first_data, second_data, third_data, None, None

    def get_tomorrow_data(city, current_time):
        first_data = Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).hour}:00')
        second_data = Weather_API.get_city_weather_data(city, index=9, header=f'{((current_time + timedelta(days=1)).hour + 3) % 24}:00')
        third_data = Weather_API.get_city_weather_data(city, index=10, header=f'{((current_time + timedelta(days=1)).hour + 6) % 24}:00')
        return first_data, second_data, third_data, None, None

    def get_3_days_data(city, current_time):
        first_data = Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.date().strftime("%b %d")}')
        second_data = Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).strftime("%b %d")}')
        third_data = Weather_API.get_city_weather_data(city, index=16, header=f'{(current_time + timedelta(days=2)).strftime("%b %d")}')
        return first_data, second_data, third_data, None, None

    def get_5_days_data(city, current_time):
        first_data = Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.strftime("%b %d")}')
        second_data = Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).strftime("%b %d")}')
        third_data = Weather_API.get_city_weather_data(city, index=16, header=f'{(current_time + timedelta(days=2)).strftime("%b %d")}')
        fourth_data = Weather_API.get_city_weather_data(city, index=24, header=f'{(current_time + timedelta(days=3)).strftime("%b %d")}')
        fifth_data = Weather_API.get_city_weather_data(city, index=32, header=f'{(current_time + timedelta(days=4)).strftime("%b %d")}')
        return first_data, second_data, third_data, fourth_data, fifth_data

