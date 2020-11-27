from django import forms
from .models import Order, OrderItem
from crispy_forms.helper import *
from crispy_forms.layout import *
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['profile','first_name', 'last_name', 'email', 'address','country','city','street',
                  'zip_code', 'phone']

class OrderItemCreateForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'store', 'product', 'price',
                  'discount_amount', 'quantity','approved']
