from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View, DetailView
from .models import City, Attraction, Rating
from .utils import query_search


class CityListView(ListView):
    model = City
    template_name = 'cities/city_list.html'
    context_object_name = 'cities'

    def get_queryset(self):
        query = self.request.GET.get("q")
        order_by = self.request.GET.get("order_by")

        if query:
            cities = query_search(query)
        else:
            cities = City.objects.all()

        if order_by and order_by != 'default':
            cities = cities.order_by(order_by)

        return cities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'City list'
        return context


'''class CityDetailView(ListView):
    model = Attraction
    template_name = 'cities/city_detail.html'
    context_object_name = 'attractions'

    def get_queryset(self):
        city_slug = self.kwargs['slug']
        city = City.objects.get(slug=city_slug)
        attractions = Attraction.objects.filter(city=city)
        return attractions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_object()
        context['title'] = 'City detail'
        context['city'] = City.objects.get(slug=self.kwargs['slug'])
        context['average_rating'] = city.get_average_rating()
        context['total_reviews'] = city.get_total_count()
        return context
    
class CityDetailView(DetailView):
    model = City
    template_name = 'cities/city_detail.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_object()  
        context['attractions'] = Attraction.objects.filter(city=city) 
        context['title'] = 'City detail'
        context['average_rating'] = city.get_average_rating() 
        context['total_reviews'] = city.get_total_count() 
        return context'''

class CityDetailView(DetailView):
    model = City
    template_name = 'cities/city_detail.html'
    context_object_name = 'city'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        return get_object_or_404(City, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_object()
        context['attractions'] = Attraction.objects.filter(city=city)
        context['title'] = 'City detail'
        context['average_rating'] = city.get_average_rating()
        context['total_reviews'] = city.get_total_count()
        return context


class RateCityView(View):
    def post(self, request, slug):
        city = get_object_or_404(City, slug=slug)
        rating_value = request.POST.get('rating')

        if rating_value:
            try:
                rating_value = int(rating_value)
                if 1 <= rating_value <= 5:
                    Rating.objects.update_or_create(
                        city=city,
                        user=request.user,
                        defaults={'rating': rating_value}
                    )
                else:
                    pass
            except ValueError:
                pass

        return redirect('cities:detail', slug=city.slug)