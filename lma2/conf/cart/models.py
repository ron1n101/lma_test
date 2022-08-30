from django.db import models
from shop.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=256, blank=True)
    data_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def total(self):
        return self.product.price * self.quantity



    def __str__(self):
        return self.product

