from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WeatherView.as_view(), name='main'),
]
