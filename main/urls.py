from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.WeatherView.as_view(), name='main'),
    path('<str:date>/', views.WeatherView.as_view(), name='weather'),
    path('search/', views.WeatherView.as_view(), name='search'),
]
