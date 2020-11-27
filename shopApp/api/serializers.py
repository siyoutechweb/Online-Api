from rest_framework import serializers
from shopApp.models import *
from orders.models import *

class ProductSerializer(serializers.ModelSerializer):
    image1 = serializers.ImageField(
            max_length=None, use_url=True
        )
    image2 = serializers.ImageField(
            max_length=None, use_url=True
        )
    image3 = serializers.ImageField(
            max_length=None, use_url=True
        )

    class Meta:
        model = Product
        fields=['id','name','slug','barcode','image1','image2','image3','short_description','description','price','discount_amount','tax','qty','warn_qty','available','promoted','category','brand','store','created','updated','sold_count']

class ProductSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['store','name','slug','barcode','short_description','description','price','discount_amount','tax','qty','warn_qty','available']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields='__all__'
        lookup_field = "name"

    #def list(self, request, *args, **kwargs):
        #res = super(StoreListView, self).list(request, *args, **kwargs)
        #res.data = {"STATUS": "SUCCESS","DATA": res.data}
        #return res

    #def to_representation(self, instance):
        #r = super(StoreSerializer, self).to_representation(instance)
        #r.update({
        #'code': '1',
        #"STATUS": "SUCCESS",
        #'DATA':r.data
        #})
        #return r

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields='__all__'

#######

#######
class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields='__all__'

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields=['version_number']
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields='__all__'
