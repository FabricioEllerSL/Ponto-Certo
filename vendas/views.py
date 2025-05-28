from django.shortcuts import render
from datetime import datetime

def display_vendas(request):
    
    today = datetime.now().strftime('%d/%m/%Y')

    context = {
        'today': today,
    }
    
    return render(request, 'vendas/display.html', context)
