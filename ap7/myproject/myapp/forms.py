# myapp/forms.py
# from django import forms
# from .models import City

# class CityForm(forms.ModelForm):
#     class Meta:
#         model = City
#         fields = '__all__'
# myapp/forms.py
from django import forms
from .models import City, Country, CountryLanguage

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country_code', 'district', 'population']

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class CountryLanguageForm(forms.ModelForm):
    class Meta:
        model = CountryLanguage
        fields = '__all__'
