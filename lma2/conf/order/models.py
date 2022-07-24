from django.db import models
from shop.models import Product

class Order(models.Model):
    f_name = models.CharField(max_length=32, blank=True, db_index=True)
    l_name = models.CharField(max_length=32, blank=True, db_index=True)
    email = models.EmailField(blank=True, db_index=True)
    address = models.CharField(max_length=256, db_index=True, blank=True)
    zip_code = models.IntegerField(blank=True, db_index=True)
    city = models.CharField(max_length=64, blank=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'

    def get_price_total(self):
        return sum(item.get_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.quantity * self.price

        