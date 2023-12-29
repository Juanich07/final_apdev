from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.views.generic import ListView
from .models import City, Country, CountryLanguage

class CityListView(ListView):
    model = City
    template_name = 'myapp/city_list.html'
    context_object_name = 'cities'

class CountryListView(ListView):
    model = Country
    template_name = 'myapp/country_list.html'
    context_object_name = 'countries'

class CountryLanguageListView(ListView):
    model = CountryLanguage
    template_name = 'myapp/country_language_list.html'
    context_object_name = 'country_languages'
