from django.contrib import admin
from .models import Order, OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','profile','first_name', 'last_name', 'email',
                    'address','country', 'city', 'zip_code', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
