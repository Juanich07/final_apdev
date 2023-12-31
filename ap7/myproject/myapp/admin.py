# from django.contrib import admin

# # Register your models here.
# # myapp/admin.py
# from django.contrib import admin
# from .models import City, Country, CountryLanguage,Continent

# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(CountryLanguage)
# admin.site.register(Continent)
# myapp/admin.py
from django.contrib import admin
# from .models import City, Country, CountryLanguage, Continent, Region, GovernmentForm

# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ['name', 'country_code', 'district', 'population']

# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ['code', 'name', 'continent', 'region', 'surface_area', 'indep_year',
#                     'population', 'life_expectancy', 'gnp', 'gnp_old', 'local_name', 
#                     'government_form', 'head_of_state', 'capital', 'code2']

# @admin.register(CountryLanguage)
# class CountryLanguageAdmin(admin.ModelAdmin):
#     list_display = ['country_code', 'language', 'is_official', 'percentage']

# @admin.register(Continent)
# class ContinentAdmin(admin.ModelAdmin):
#     list_display = ['name']

# @admin.register(Region)
# class RegionAdmin(admin.ModelAdmin):
#     list_display = ['name', 'continent']

# @admin.register(GovernmentForm)
# class GovernmentFormAdmin(admin.ModelAdmin):
#     list_display = ['name']
# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ['code', 'name', 'get_continents', 'region', 'surface_area', 'indep_year',
#                     'population', 'life_expectancy', 'gnp', 'gnp_old', 'local_name', 
#                     'government_form', 'head_of_state', 'capital', 'code2']

#     def get_continents(self, obj):
#         return ', '.join([continent.name for continent in obj.continents.all()])

#     get_continents.short_description = 'Continents'
from django.contrib import admin
from .models import City, Country, CountryLanguage, Continent, Region, GovernmentForm

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country_code', 'district', 'population']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'get_continents', 'region', 'surface_area', 'indep_year',
                    'population', 'life_expectancy', 'gnp', 'gnp_old', 'local_name', 
                    'government_form', 'head_of_state', 'capital', 'code2']

    def get_continents(self, obj):
        return ', '.join([continent.name for continent in obj.continents.all()])

    get_continents.short_description = 'Continents'

@admin.register(CountryLanguage)
class CountryLanguageAdmin(admin.ModelAdmin):
    list_display = ['country_code', 'language', 'is_official', 'percentage']

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'continent']

@admin.register(GovernmentForm)
class GovernmentFormAdmin(admin.ModelAdmin):
    list_display = ['name']
