from django.shortcuts import render, get_object_or_404, redirect
from .models import City, Country, CountryLanguage
from .forms import CityForm, CountryForm, CountryLanguageForm

# City views (previously provided)

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'myapp/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'myapp/country_detail.html', {'country': country})

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm()
    return render(request, 'myapp/country_form.html', {'form': form})

def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'myapp/country_form.html', {'form': form, 'country': country})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country_list')
    return render(request, 'myapp/country_confirm_delete.html', {'country': country})

# Similar views for CountryLanguage (list, detail, create, update, delete)
def country_language_list(request):
    country_languages = CountryLanguage.objects.all()
    return render(request, 'myapp/country_language_list.html', {'country_languages': country_languages})

def country_language_detail(request, pk):
    language = get_object_or_404(CountryLanguage, pk=pk)
    return render(request, 'myapp/country_language_detail.html', {'language': language})

def country_language_create(request):
    if request.method == 'POST':
        form = CountryLanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('country_language_detail', pk=language.pk)
    else:
        form = CountryLanguageForm()
    return render(request, 'myapp/country_language_form.html', {'form': form})

def country_language_update(request, pk):
    language = get_object_or_404(CountryLanguage, pk=pk)
    if request.method == 'POST':
        form = CountryLanguageForm(request.POST, instance=language)
        if form.is_valid():
            language = form.save()
            return redirect('country_language_detail', pk=language.pk)
    else:
        form = CountryLanguageForm(instance=language)
    return render(request, 'myapp/country_language_form.html', {'form': form, 'language': language})

def country_language_delete(request, pk):
    language = get_object_or_404(CountryLanguage, pk=pk)
    if request.method == 'POST':
        language.delete()
        return redirect('country_language_list')
    return render(request, 'myapp/country_language_confirm_delete.html', {'language': language})

def city_list(request):
    cities = City.objects.all()
    return render(request, 'myapp/city_list.html', {'cities': cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'myapp/city_detail.html', {'city': city})

def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm()
    return render(request, 'myapp/city_form.html', {'form': form})

def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'myapp/city_form.html', {'form': form, 'city': city})

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('city_list')
    return render(request, 'myapp/city_confirm_delete.html', {'city': city})

def home(request):
    return render(request, 'myapp/home.html')
