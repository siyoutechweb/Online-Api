from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django_simple_coupons.models import Coupon

class ParentCategory(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)

    slug = models.SlugField(max_length=200,
                            unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'parent_category'
        verbose_name_plural = 'parent_categories'
    def __str__(self):
        return self.name

class Category(models.Model):
    parentcategory = models.ForeignKey(ParentCategory,
                                 related_name='categories',
                                 on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200,
                            db_index=True)
    name_it = models.CharField(max_length=200,
                             db_index=True)
    name_cn = models.CharField(max_length=200,
                             db_index=True)
    name_fr = models.CharField(max_length=200,
                             db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shopApp:product_list_by_category',
                       args=[self.slug])

class Brand(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    available = models.BooleanField(default=False)
    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=200,db_index=True,unique=True)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200,default='USA')
    city = models.CharField(max_length=200,default='USA')
    street = models.CharField(max_length=200,default='USA')
    zip_code = models.IntegerField(default='1000')
    phone = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    raiting=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    like_count=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    orders_count=models.IntegerField(default=0)
    description=models.CharField(max_length=200,blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'store'
        verbose_name_plural = 'stores'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return 'https://online.com:8000'

#############
class Supplier(models.Model):

    supplier_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=50)
    img_url = models.CharField(max_length=255,blank=True)
    img_name = models.CharField(max_length=255,blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website =models.CharField(max_length=255,blank=True)
    adress =models.CharField(max_length=255,blank=True)
    country =models.CharField(max_length=255,blank=True)
    city =models.CharField(max_length=255,blank=True)
    contact =models.CharField(max_length=255,blank=True)
    tax_id =models.CharField(max_length=255)
    province=models.CharField(max_length=255,blank=True)
    postal_code =models.CharField(max_length=255,blank=True)

class Product(models.Model):
    supplier_id=models.ForeignKey(Supplier,related_name='products',on_delete=models.CASCADE ,default=1)

    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,default=3)
    brand = models.ForeignKey(Brand,
                                 related_name='products',
                                 on_delete=models.CASCADE,default=1)
    store=models.ForeignKey(Store,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    barcode = models.CharField(max_length=200,default='123456789')
    image1 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    short_description = models.TextField(max_length=100,blank=True)
    description = models.TextField(max_length=900,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    log_x=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    log_y=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    log_z=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    tag = models.CharField(max_length=30, db_index=True,default='Product')
    like_count=models.IntegerField(default=0)
    raiting=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    qty=models.IntegerField(default=1)
    warn_qty=models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    promoted = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    sold_count=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shopApp:product_detail',
                       args=[self.id, self.slug])

    def cal_price(self):
        if (self.discount_amount>0):
            self.price=self.price-self.discount_amount
        return self.price



    def update_qty(self, amount):
        if (self.qty-amount>0):
            self.qty=self.qty-amount
            return True
        else:
            return False
class CouponProduct(models.Model):
        product=models.ForeignKey(Product,related_name='product', on_delete=models.CASCADE)
        coupon=models.ForeignKey(Coupon,related_name='coupon', on_delete=models.CASCADE)
class GroupSale(models.Model):
        #store=models.ForeignKey(Store,related_name='products',on_delete=models.CASCADE)
        user=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
        product=models.ForeignKey(Product,related_name='products', on_delete=models.CASCADE)
        quantity=models.IntegerField(default=1)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        start_date=models.DateTimeField()
        end_date=models.DateTimeField()



##############
class Comment(models.Model):
    product = models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Version(models.Model):
    version_number=models.CharField(max_length=200,default='1.0.0+1')
