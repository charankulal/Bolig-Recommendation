from django.urls import path
from .views import address_autocomplete, home, recommend_page

urlpatterns = [
    path('', home, name='home'),
    path('recommend', recommend_page, name='recommend'),
    path('autocomplete/', address_autocomplete, name='address_autocomplete'),
]