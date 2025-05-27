from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'textarea-field', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'input-field', 'step': '0.01'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'input-field', 'min': 0}),
        }