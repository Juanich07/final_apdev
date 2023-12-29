# myapp/urls.py
from django.urls import path
from .views import CityListView, CountryListView, CountryLanguageListView

app_name = 'myapp'

urlpatterns = [
    path('cities/', CityListView.as_view(), name='city_list'),
    path('countries/', CountryListView.as_view(), name='country_list'),
    path('country-languages/', CountryLanguageListView.as_view(), name='country_language_list'),
    # Add more URLs as needed
]
