from django.db import models
from account.models import Profile
from shopApp.models import Product, Store
import datetime
class Order(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=200,default='No country configured yet')
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200,default='No street configured yet')
    zip_code = models.IntegerField(default='1234')
    phone = models.CharField(max_length=200,default='No phone number configured yet')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_total_discount(self):
        return sum(item.get_discount() for item in self.items.all())
    def get_total_cost_after_discount(self):
        x=self.get_total_cost()
        y=self.get_total_discount()
        z=x-y
        return z

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount=models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    approved = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity
    def get_discount(self):
        return self.discount_amount * self.quantity
