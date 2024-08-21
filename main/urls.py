from django.urls import path, include
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.WeatherView.as_view(), name='weather'),
    path('search/', views.WeatherView.as_view(), name='search'),
]
