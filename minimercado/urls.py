from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('estoque/', include('estoque.urls')),
    path('vendas/', include('vendas.urls')),
]
