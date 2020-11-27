from rest_framework import generics
from ..models import *
from .serializers import *
from orders.models import *
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from django.db.models import Count
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

class ProductListView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
##############
class SupplierListView(generics.ListAPIView):
    queryset= Supplier.objects.all()
    serializer_class=SupplierSerializer
##############
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
class StoreDetailView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = "name"
    lookup_value_regex = "[^/]+"

class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ParentCategoryListView(generics.ListAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer
class ParentCategoryDetailView(generics.RetrieveAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer

class VersionDetailView(generics.RetrieveAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

@api_view(['POST',])

def api_create_brand(request):
    serializer=BrandSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST',])

def api_create_product(request):
    serializer=ProductSerializerPOST(data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class PopularStoresListView(generics.ListAPIView):
    queryset = Store.objects.filter(orders_count__gt=9)
    serializer_class = StoreSerializer

class FeaturedStoresListView(generics.ListAPIView):
    queryset = Store.objects.filter(featured=True)
    serializer_class = StoreSerializer

class NewStoresListView(generics.ListAPIView):
    queryset = Store.objects.all().order_by('-id')
    serializer_class = StoreSerializer


class PopularProductsListView(generics.ListAPIView):
    queryset = Product.objects.filter(sold_count__gt=9)
    serializer_class = ProductSerializer

class FeaturedProductsListView(generics.ListAPIView):
    queryset = Product.objects.filter(promoted=True)
    serializer_class = ProductSerializer

class NewProductsListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

#######
#APIs_Product
@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def api_productlist(request):
    if request.method=='GET':
        products=Product.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(products, request)
        serializer=ProductSerializerPOST(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
        #return Response(serializer.data)
    #elif request.method=='POST':
        #serializer=ProductSerializerPOST(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_productdetails(request,pk):
    try:
        product=Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=ProductSerializerPOST(product)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=ProductSerializerPOST(product,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Category
@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def api_categorylist(request):
    if request.method=='GET':
        categorys=Category.objects.all()
        serializer=CategorySerializer(categorys,many=True)
        return Response(serializer.data)
    #elif request.method=='POST':
        #serializer=CategorySerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_categorydetails(request,pk):
    try:
        categorys=Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=CategorySerializer(categorys)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=CategorySerializer(categorys,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            categorys.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_ParentsCategory
@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def api_parentcategorylist(request):
    if request.method=='GET':
        categorys=ParentCategory.objects.all()
        serializer=ParentCategorySerializer(categorys,many=True)
        return Response(serializer.data)
    #elif request.method=='POST':
        #serializer=ParentCategorySerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_parentcategorydetails(request,pk):
    try:
        categorys=ParentCategory.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=ParentCategorySerializer(categorys)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=ParentCategorySerializer(categorys,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            categorys.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Brand
@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def api_brandslist(request):
    if request.method=='GET':
        brands=Brand.objects.all()
        serializer=BrandSerializer(brands,many=True)
        return Response(serializer.data)
    #elif request.method=='POST':
        #serializer=BrandSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_brandsdetails(request,pk):
    try:
        brands=Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=BrandSerializer(brands)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=BrandSerializer(brands,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            brands.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Store
@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def api_storelist(request):
    if request.method=='GET':

        #authentication_classes=[BasicAuthentication]
        #permissions_classes=[IsAuthenticated,DjangoModelPermissions]
        stores=Store.objects.all()
        #ct=Store.objects.count()
        serializer=StoreSerializer(stores,many=True)

        return Response(serializer.data)

    #elif request.method=='POST':
        #serializer=StoreSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_storedetails(request,pk):
    try:
        stores=Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=StoreSerializer(stores)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=StoreSerializer(stores,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            stores.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Supplier
@api_view(['POST','GET'])
@authentication_classes(())
@permission_classes(())
def api_supplierlist(request):
    if request.method=='GET':
        suppliers=Supplier.objects.all()
        serializer=SupplierSerializer(suppliers,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_supplierdetails(request,pk):
    try:
        suppliers=Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=SupplierSerializer(suppliers)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=SupplierSerializer(suppliers,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            suppliers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Comment
@api_view(['POST','GET'])
def api_commentlist(request):
    if request.method=='GET':
        comments=Comment.objects.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def api_commentdetails(request,pk):
    try:
        comments=Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=CommentSerializer(comments)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=CommentSerializer(comments,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            comments.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_like
@api_view(['POST','GET'])
def api_likelist(request):
    if request.method=='GET':
        like=Like.objects.all()
        serializer=LikeSerializer(like,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def api_likedetails(request,pk):
    try:
        like=Like.objects.get(pk=pk)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=LikeSerializer(like)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=LikeSerializer(like,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_Order

@api_view(['POST','GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def api_orderslist(request):
    if request.method=='GET':
        
            order=Order.objects.all()
            serializer=OrderSerializer(order,many=True)
            return Response(serializer.data)
    elif request.method=='POST':
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_orderdetails(request,pk):
    try:
        order=Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=OrderSerializer(order)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=OrderSerializer(order,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#APIs_OrderItem
@api_view(['POST','GET'])
@authentication_classes(())
@permission_classes(())
def api_ordersitemlist(request):
    if request.method=='GET':
        order=OrderItem.objects.all()
        serializer=OrderItemSerializer(order,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
@authentication_classes(())
@permission_classes(())
def api_orderitemdetails(request,pk):
    try:
        order=OrderItem.objects.get(pk=pk)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            serializer=OrderItemSerializer(order)
            return Response(serializer.data)
    elif request.method=='PUT':
            serializer=OrderItemSerializer(order,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST',])
@authentication_classes(())
@permission_classes(())
def api_create_supplier(request):
    serializer=SupplierSerializer(data=request.data)
    data={}

    if serializer.is_valid():
        serializer.save()
        #serializer =+ dataa
        return Response(serializer.data)
    return Response(serializer.errors)

#######
