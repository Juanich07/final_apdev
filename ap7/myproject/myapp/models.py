# from django.db import models

# # Create your models here.
# # myapp/models.py
# from django.db import models
# from django.utils import timezone

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         app_label = 'myapp'

# class City(BaseModel):
#     name = models.CharField(max_length=100)
#     country_code = models.CharField(max_length=3)
#     district = models.CharField(max_length=100)
#     population = models.IntegerField()

#     def __str__(self):
#         return self.name

# class Country(BaseModel):
#     code = models.CharField(max_length=3, unique=True)
#     name = models.CharField(max_length=100)
#     continent = models.CharField(max_length=50)
    
#     surface_area = models.FloatField()
#     indep_year = models.IntegerField(null=True, blank=True)
#     population = models.IntegerField()
#     life_expectancy = models.FloatField(null=True, blank=True)
#     gnp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     gnp_old = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     local_name = models.CharField(max_length=100)
#     government_form = models.CharField(max_length=100)
#     head_of_state = models.CharField(max_length=100)
#     capital = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
#     code2 = models.CharField(max_length=2)

#     def __str__(self):
#         return self.name

# class CountryLanguage(BaseModel):
#     country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
#     language = models.CharField(max_length=50)
#     is_official = models.BooleanField()
#     percentage = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.country_code} - {self.language}"
# myapp/models.py
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'myapp'

class City(BaseModel):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    district = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Country(BaseModel):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    surface_area = models.FloatField()
    indep_year = models.IntegerField(null=True, blank=True)
    population = models.IntegerField()
    life_expectancy = models.FloatField(null=True, blank=True)
    gnp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gnp_old = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    local_name = models.CharField(max_length=100)
    government_form = models.CharField(max_length=100)
    head_of_state = models.CharField(max_length=100)
    capital = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    code2 = models.CharField(max_length=2)
    flag = models.ImageField(upload_to='country_flags/', null=True, blank=True)

    def __str__(self):
        return self.name

class CountryLanguage(BaseModel):
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    is_official = models.BooleanField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.country_code} - {self.language}"

class Continent(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Region(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.continent})"

class GovernmentForm(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

