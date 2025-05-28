from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import datetime
from .forms import ProductForm

@login_required(login_url='home:user_login')
def display_products(request):

    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    today = datetime.now().strftime('%d/%m/%Y')

    context = {
        'today': today,
        'products': products,
    }
    
    return render(request, 'estoque/display.html', context)

@login_required(login_url='home:user_login')
def create_product(request):

    today = datetime.now().strftime('%d/%m/%Y')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:display_products')
    else:
        form = ProductForm()

    context = {
        'form': form,
        'today': today,
    }

    return render(request, 'estoque/create.html', context)

@login_required(login_url='home:user_login')
def update_product(request, id):

    today = datetime.now().strftime('%d/%m/%Y')

    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('estoque:display_products')
    else:
        form = ProductForm(instance=product)


    context = {
        'form': form,
        'today': today,
    }

    return render(request, 'estoque/create.html', context)

@login_required(login_url='home:user_login')
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('estoque:display_products')
