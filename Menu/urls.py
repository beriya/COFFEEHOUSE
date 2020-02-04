from django.contrib import admin
from django.urls import path, include
from .views import Menu

app_name = "Menu"

urlpatterns = [
    
    path('', Menu, name = 'Menu'),

]
