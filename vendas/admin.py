from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'sale_date')
    search_fields = ('product__name',)
    list_filter = ('sale_date',)