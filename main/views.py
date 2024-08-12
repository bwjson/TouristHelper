from django.views.generic import TemplateView
from .utils import weather_api as w


class WeatherView(TemplateView):
    template_name = 'main/weather.html'

    def get_context_data(self, **kwargs):
        # date = self.request.GET.get('date', None)

        search_city = self.request.GET.get('city', None)

        if search_city is None:
            current_data = w.Weather_API.get_weather_data(53.2194, 63.6354, index=0)
            tomorrow_data = w.Weather_API.get_weather_data(53.2194, 63.6354, index=8)
            day_after_data = w.Weather_API.get_weather_data(53.2194, 63.6354, index=16)

            current = w.Weather_API(**current_data)
            tomorrow = w.Weather_API(**tomorrow_data)
            day_after = w.Weather_API(**day_after_data)
        else:
            search_city_data_c = w.Weather_API.get_city_weather_data(search_city, index=0)
            search_city_data_t = w.Weather_API.get_city_weather_data(search_city, index=8)
            search_city_data_d = w.Weather_API.get_city_weather_data(search_city, index=16)
            current = w.Weather_API(**search_city_data_c)
            tomorrow = w.Weather_API(**search_city_data_t)
            day_after = w.Weather_API(**search_city_data_d)

        context = super().get_context_data(**kwargs)
        context['title'] = 'Weather'
        context['weather'] = {
            'current': current,
            'tomorrow': tomorrow,
            'day_after': day_after,
        }
        return context


