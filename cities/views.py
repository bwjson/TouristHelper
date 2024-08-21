from django.shortcuts import render


def CitiesView(request):
    return render(request, 'cities/city_list.html', {'title': 'Cities'})

