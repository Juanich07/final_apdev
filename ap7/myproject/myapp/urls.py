# myapp/urls.py
# # myapp/urls.py
# from django.urls import path
# from .views import city_list, city_detail, city_create, city_update, city_delete

# urlpatterns = [
#     path('cities/', city_list, name='city_list'),
#     path('cities/<int:pk>/', city_detail, name='city_detail'),
#     path('cities/new/', city_create, name='city_create'),
#     path('cities/<int:pk>/edit/', city_update, name='city_update'),
#     path('cities/<int:pk>/delete/', city_delete, name='city_delete'),
# ]
# myapp/urls.py
# from django.urls import path
# from .views import city_list, city_detail, city_create, city_update, city_delete, default_view

# urlpatterns = [
#     path('', default_view, name='default_view'),  # Add this line
#     path('cities/', city_list, name='city_list'),
#     path('cities/<int:pk>/', city_detail, name='city_detail'),
#     path('cities/new/', city_create, name='city_create'),
#     path('cities/<int:pk>/edit/', city_update, name='city_update'),
#     path('cities/<int:pk>/delete/', city_delete, name='city_delete'),
# ]
# myapp/urls.py
from django.urls import path
from .views import city_list, city_detail, city_create, city_update, city_delete
from .views import country_list, country_detail, country_create, country_update, country_delete
from .views import country_language_list, country_language_detail, country_language_create, country_language_update, country_language_delete
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('cities/', city_list, name='city_list'),
    path('cities/<int:pk>/', city_detail, name='city_detail'),
    path('cities/new/', city_create, name='city_create'),
    path('cities/<int:pk>/edit/', city_update, name='city_update'),
    path('cities/<int:pk>/delete/', city_delete, name='city_delete'),

    path('countries/', country_list, name='country_list'),
    path('countries/<int:pk>/', country_detail, name='country_detail'),
    path('countries/new/', country_create, name='country_create'),
    path('countries/<int:pk>/edit/', country_update, name='country_update'),
    path('countries/<int:pk>/delete/', country_delete, name='country_delete'),

    path('country-languages/', country_language_list, name='country_language_list'),
    path('country-languages/<int:pk>/', country_language_detail, name='country_language_detail'),
    path('country-languages/new/', country_language_create, name='country_language_create'),
    path('country-languages/<int:pk>/edit/', country_language_update, name='country_language_update'),
    path('country-languages/<int:pk>/delete/', country_language_delete, name='country_language_delete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)