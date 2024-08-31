from django.urls import path, include
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.CityListView.as_view(), name='list'),
    path('search/', views.CityListView.as_view(), name='search'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='detail'),
    path('rate-city/<slug:slug>/', views.RateCityView.as_view(), name='rate_city'),
    path('<slug:slug>/<slug:attr_slug>/', views.AttractionDetailView.as_view(), name='attr_detail'),
    path('add_review-attr/<slug:city_slug>/<slug:attr_slug>/', views.AddReviewAttrView.as_view(), name='add_review_attr'),
	path('remove_review-attr/<slug:city_slug>/<slug:attr_slug>/<int:pk>/', views.RemoveReviewAttrView.as_view(), name='remove_review_attr')
]
