from django.urls import path
from .views import album_page

urlpatterns =[
    path('', album_page, name='album'),
]