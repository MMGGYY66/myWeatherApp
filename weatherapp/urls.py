from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.weatherview, name='weather'),
    path('about.html', views.about, name='about'),
]
