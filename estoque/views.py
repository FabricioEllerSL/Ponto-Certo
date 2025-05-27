from django.shortcuts import render
from .models import Product

def display_products(request):
    
    products = Product.objects.all()
    
    return render(request, 'estoque/display.html', {'products': products})
