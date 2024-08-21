from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='main'),
    path('weather/', include('main.urls'), name='weather'),
    path('user/', include('user.urls'), name='user'),
    path('cities/', include('cities.urls'), name='cities'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)