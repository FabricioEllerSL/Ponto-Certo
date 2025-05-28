from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'sale-select',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'sale-input',
                'min': '1',
            }),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
        }