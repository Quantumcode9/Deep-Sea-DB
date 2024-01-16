from django.contrib import admin

# Register your models here.

from .models import Creature

admin.site.register(Creature)

# Path: catcollector/main_app/urls.py

from django.urls import path

from . import views

# this is how we map a url to a view

#views.home is the function home in views.py in main_app

#name='home' is the name of the route

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    
    path('creature/', views.creature_index, name='index'),
    ]