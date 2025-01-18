from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .utils import weather_api as w
from main.utils.api_client import APIClient as api
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
            first_data, second_data, third_data, fourth_data, fifth_data = api.get_today_data(city, current_time)
        elif date == 'tomorrow':
            first_data, second_data, third_data, fourth_data, fifth_data = api.get_tomorrow_data(city, current_time)
        elif date == '5_days':
            first_data, second_data, third_data, fourth_data, fifth_data = api.get_5_days_data(city, current_time)
        elif date == '3_days':
            first_data, second_data, third_data, fourth_data, fifth_data = api.get_3_days_data(city, current_time)
        else:
            first_data = None
            second_data = None
            third_data = None

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


class HomePage(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': 'Home Page'}