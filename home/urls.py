from django.contrib import admin
from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('navigation/', views.navigation, name='navigation'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]