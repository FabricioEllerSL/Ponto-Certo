from django.db import models
from estoque.models import Product

class Sale(models.Model):

    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')

    def __str__(self):
        return f"{self.product.name} - {self.quantity} - {self.sale_date}"
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"