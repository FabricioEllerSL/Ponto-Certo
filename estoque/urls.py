from django.urls import path
from estoque import views

app_name = 'estoque'

urlpatterns = [
    path('', views.display_products, name='display_products'),
    path('create', views.create_product, name='create_product'),
    path('update/<int:id>', views.update_product, name='update_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
]