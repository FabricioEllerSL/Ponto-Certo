from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Sale
from .forms import SaleForm

def display_vendas(request):

    query = request.GET.get('q')

    sales = Sale.objects.all()

    if query:
        sales = sales.filter(product__name__icontains=query)
    
    today = datetime.now().strftime('%d/%m/%Y')

    context = {
        'today': today,
        'sales': sales,
    }
    
    return render(request, 'vendas/display.html', context)

def create_venda(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            product = venda.product

            if venda.quantity > product.stock_quantity:
                messages.error(request, f"Estoque insuficiente! O produto '{product.name}' possui apenas {product.stock_quantity} unidades disponíveis.")
                return redirect('vendas:create_venda')
            else:
                # Atualiza o estoque e salva a venda
                product.stock_quantity -= venda.quantity
                product.save()
            venda.save()
            return redirect('vendas:display_vendas')
    else:
        form = SaleForm()

    context = {
        'form': form,
    }
    return render(request, 'vendas/create.html', context)
