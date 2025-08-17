from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('recommend', recommend_page, name='recommend'),
    path('autocomplete/', address_autocomplete, name='address_autocomplete'),
    path('recommendations/', recommendations, name='recommendations'),
]