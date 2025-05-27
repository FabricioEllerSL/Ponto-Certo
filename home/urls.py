from django.contrib import admin
from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('navigation', views.navigation, name='navigation'),
]