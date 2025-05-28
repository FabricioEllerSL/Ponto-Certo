from django.contrib import admin
from django.urls import path
from vendas import views

app_name = 'vendas'

urlpatterns = [
    path('', views.display_vendas, name='display_vendas'),
    path('create/', views.create_venda, name='create_venda'),
]