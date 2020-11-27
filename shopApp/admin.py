from django.contrib import admin
from .models import *
from django_simple_coupons.models import Coupon

#########
@admin.register(CouponProduct)
class CouponProductAdmin(admin.ModelAdmin):
    list_display =  ['id','product','coupon']

@admin.register(GroupSale)
class GroupSaleAdmin(admin.ModelAdmin):
    list_display =  ['id','product','quantity','price','start_date','end_date']

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
        list_display = ['supplier_name', 'company_name','email','tax_id','created_at','updated_at']
        #prepopulated_fields = {'tax_id': ('supplier_name','company_name')}

#########

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['id','version_number']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body','created','updated']
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','created']

# you will need this later, future me
# class AuthorAdmin(admin.ModelAdmin):
    # list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
