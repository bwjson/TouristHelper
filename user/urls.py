from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]