from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .utils import weather_api as w
from datetime import datetime, timedelta


class WeatherView(LoginRequiredMixin, TemplateView):
    template_name = 'main/weather.html'

    def get_context_data(self, **kwargs):
        search_city = self.request.GET.get('city', None)
        date = self.request.GET.get('date', 'today')
        profile_city = self.request.user.city
        current_time = datetime.now()

        if not search_city and not profile_city:
            context = super().get_context_data(**kwargs)
            context['error'] = 'Please enter the name of the city first'
            context['weather'] = {'date': date}
            return context

        city = search_city if search_city else profile_city

        if date == 'today':
            first_data = w.Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.hour}:00')
            second_data = w.Weather_API.get_city_weather_data(city, index=1, header=f'{(current_time.hour + 3) % 24}:00')
            third_data = w.Weather_API.get_city_weather_data(city, index=2, header=f'{(current_time.hour + 6) % 24}:00')
            fourth_data = None
            fifth_data = None
        elif date == 'tomorrow':
            first_data = w.Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).hour}:00')
            second_data = w.Weather_API.get_city_weather_data(city, index=9, header=f'{((current_time + timedelta(days=1)).hour + 3) % 24}:00')
            third_data = w.Weather_API.get_city_weather_data(city, index=10, header=f'{((current_time + timedelta(days=1)).hour + 6) % 24}:00')
            fourth_data = None
            fifth_data = None
        elif date == '5_days':
            first_data = w.Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.strftime("%b %d")}')
            second_data = w.Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).strftime("%b %d")}')
            third_data = w.Weather_API.get_city_weather_data(city, index=16, header=f'{(current_time + timedelta(days=2)).strftime("%b %d")}')
            fourth_data = w.Weather_API.get_city_weather_data(city, index=24, header=f'{(current_time + timedelta(days=3)).strftime("%b %d")}')
            fifth_data = w.Weather_API.get_city_weather_data(city, index=32, header=f'{(current_time + timedelta(days=4)).strftime("%b %d")}')
        elif date == '3_days':
            first_data = w.Weather_API.get_city_weather_data(city, index=0, header=f'{current_time.date().strftime("%b %d")}')
            second_data = w.Weather_API.get_city_weather_data(city, index=8, header=f'{(current_time + timedelta(days=1)).strftime("%b %d")}')
            third_data = w.Weather_API.get_city_weather_data(city, index=16, header=f'{(current_time + timedelta(days=2)).strftime("%b %d")}')
            fourth_data = None
            fifth_data = None
        else:
            first_data = None

        if first_data == 'City not found' or first_data is None:
            context = super().get_context_data(**kwargs)
            context['error'] = 'There is no data for that city'
            return context

        first = w.Weather_API(**first_data)
        second = w.Weather_API(**second_data)
        third = w.Weather_API(**third_data)

        if date == '5_days':
            fourth = w.Weather_API(**fourth_data)
            fifth = w.Weather_API(**fifth_data)


        context = super().get_context_data(**kwargs)
        context['title'] = 'Weather'
        context['weather'] = {
            'first': first,
            'second': second,
            'third': third,
            'fourth': fourth if date == '5_days' else None,
            'fifth': fifth if date == '5_days' else None,
            'date': date
        }
        return context


