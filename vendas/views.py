from django.shortcuts import render
from datetime import datetime
from .models import Sale

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
