from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    """
    Render the home page.
    """

    today = datetime.now().strftime('%d/%m/%Y')
    context = {
        'today': today,
    }

    return render(request, 'home/index.html', context)

def navigation(request):
    """
    Render the navigation page.
    """

    today = datetime.now().strftime('%d/%m/%Y')
    context = {
        'today': today,
    }
    
    return render(request, 'home/navigation.html', context)