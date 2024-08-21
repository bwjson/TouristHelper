from django.urls import path, include
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.CitiesView, name='list'),
]
