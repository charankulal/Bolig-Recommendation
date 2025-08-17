from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('recommend', recommend_page, name='recommend'),
    path('recommendations/', recommendations, name='recommendations'),
]