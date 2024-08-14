from django.views.generic import TemplateView
from .utils import weather_api as w


class WeatherView(TemplateView):
    template_name = 'main/weather.html'

    def get_context_data(self, **kwargs):
        search_city = self.request.GET.get('city', 'Tokyo')
        date = self.request.GET.get('date', '3_days')

        if date == 'today':
            first_data = w.Weather_API.get_city_weather_data(search_city, index=0)
            second_data = w.Weather_API.get_city_weather_data(search_city, index=2)
            third_data = w.Weather_API.get_city_weather_data(search_city, index=4)
            fourth_data = None
            fifth_data = None
        elif date == 'tomorrow':
            first_data = w.Weather_API.get_city_weather_data(search_city, index=8)
            second_data = w.Weather_API.get_city_weather_data(search_city, index=10)
            third_data = w.Weather_API.get_city_weather_data(search_city, index=12)
            fourth_data = None
            fifth_data = None
        elif date == '5_days':
            first_data = w.Weather_API.get_city_weather_data(search_city, index=0)
            second_data = w.Weather_API.get_city_weather_data(search_city, index=8)
            third_data = w.Weather_API.get_city_weather_data(search_city, index=16)
            fourth_data = w.Weather_API.get_city_weather_data(search_city, index=24)
            fifth_data = w.Weather_API.get_city_weather_data(search_city, index=32)
        else:
            first_data = w.Weather_API.get_city_weather_data(search_city, index=0)
            second_data = w.Weather_API.get_city_weather_data(search_city, index=8)
            third_data = w.Weather_API.get_city_weather_data(search_city, index=16)
            fourth_data = None
            fifth_data = None

        first = w.Weather_API(**first_data)
        second = w.Weather_API(**second_data)
        third = w.Weather_API(**third_data)

        if date == '5_days':
            fourth = w.Weather_API(**fourth_data)
            fifth = w.Weather_API(**fifth_data)

        if first_data == 'City not found' or first_data is None:
            context = super().get_context_data(**kwargs)
            context['error'] = 'City not found'
            return context

        print(date)

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


