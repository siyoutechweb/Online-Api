from django.urls import path
from . import views
from django.http import HttpResponse
app_name = 'shopAppApi'
urlpatterns = [
#Products
    path('products/create/',
         views.api_create_product,
         name='create_product'),
    path('products/',
         views.ProductListView.as_view(),
         name='products_list'),
    path('products/popular',
         views.PopularProductsListView.as_view(),
         name='popular_products_list'),

    path('products/featured',
         views.FeaturedProductsListView.as_view(),
         name='featured_products_list'),


    path('products/new',
         views.NewProductsListView.as_view(),
         name='new_products_list'),

    path('products/<pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),


#categories

    path('categories/',
         views.CategoryListView.as_view(),
         name='categories_list'),
    path('categories/<pk>',
         views.CategoryDetailView.as_view(),
         name='category_detail'),

#Stores

    path('stores/',
         views.StoreListView.as_view(),
         name='stores_list'),
    path('stores/popular',
         views.PopularStoresListView.as_view(),
         name='popular_stores_list'),
    path('stores/featured',
         views.FeaturedStoresListView.as_view(),
         name='featured_stores_list'),

    path('stores/new',
         views.NewStoresListView.as_view(),
         name='featured_stores_list'),


    path('stores/<pk>',
         views.StoreDetailView.as_view(),
         name='store_detail'),
    path('stores/byname/<name>',
         views.StoreDetailView.as_view(),
         name='store_detail_by_name'),
#Brands

    path('brands/',
         views.BrandListView.as_view(),
         name='brands_list'),
    path('brands/<pk>',
         views.BrandDetailView.as_view(),
         name='brand_detail'),
    path('brands/create/',
         views.api_create_brand,
         name='create_brand'),

#Orders
    path('orders/',
         views.OrderListView.as_view(),
         name='orders_list'),
    path('orders/<pk>',
         views.OrderDetailView.as_view(),
         name='orders_detail'),
#Parent Categories
    path('parentcategories/',
         views.ParentCategoryListView.as_view(),
         name='parent_categories_list'),
    path('parentcategories/<pk>',
         views.ParentCategoryDetailView.as_view(),
         name='parent_category_detail'),
# Version
    path('version/<pk>',
         views.VersionDetailView.as_view(),
         name='version_number'),
###################
#Product
    path('productlist/',
         views.api_productlist,
         name='productslists'),
     path('productdetails/<pk>',
          views.api_productdetails,
          name='productsdetails'),

#Category
    path('categorylist/',
         views.api_categorylist,
         name='categorylists'),
    path('categorydetails/<pk>',
         views.api_categorydetails,
         name='categorysdetails'),
#ParentCategory
    path('parentcategorylist/',
         views.api_parentcategorylist,
         name='parentcategorylists'),
    path('parentcategorydetails/<pk>',
         views.api_parentcategorydetails,
         name='parentcategorysdetails'),
#Brand
    path('brandslist/',
         views.api_brandslist,
         name='brandlists'),
    path('branddetails/<pk>',
         views.api_brandsdetails,
         name='branddetails'),

#Store
    path('storelist/',
         views.api_storelist,
         name='storelists'),
    path('storedetails/<pk>',
         views.api_storedetails,
         name='storedetails'),
#supplier
    path('supplierslist/',
         views.api_supplierlist,
         name='supplierlists'),

    path('supplierdetails/<pk>',
         views.api_supplierdetails,
         name='supplierdetails'),
#comment
    path('commentslist/',
         views.api_commentlist,
         name='commentslists'),
    path('commentdetails/<pk>',
         views.api_commentdetails,
         name='commentdetails'),
#Like
    path('likeslist/',
         views.api_likelist,
         name='likeslists'),
    path('likedetails/<pk>',
         views.api_likedetails,
         name='likedetails'),

#order
    path('orderslist',
         views.api_orderslist,
         name='ordersslists'),
    path('orderdetails/<pk>',
         views.api_orderdetails,
         name='ordrerdetails'),

#orderitem
    path('ordersitemlist/',
         views.api_ordersitemlist,
         name='ordersslists'),
    path('orderitemdetails/<pk>',
         views.api_orderitemdetails,
         name='ordrerdetails'),


]
