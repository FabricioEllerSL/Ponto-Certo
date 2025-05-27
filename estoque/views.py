from django.shortcuts import render, redirect
from .models import Product
from datetime import datetime
from .forms import ProductForm

def display_products(request):

    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    today = datetime.now().strftime('%d/%m/%Y')
    context = {
        'today': today,
    }
    
    return render(request, 'estoque/display.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:display_products')
    else:
        form = ProductForm()
    return render(request, 'estoque/create.html', {'form': form})
