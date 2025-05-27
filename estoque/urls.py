from django.urls import path
from estoque import views

app_name = 'estoque'

urlpatterns = [
    path('', views.display_products, name='display_products'),
]