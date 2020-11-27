from django.urls import path
from . import views
app_name = 'shopApp'
urlpatterns = [
    path('upload_brand/', views.brand_upload, name='brand_upload'),
    path('upload_category/',views.category_upload, name='category_upload'),
    path('export_category/',views.export_to_csv,name='export_category'),
    path('show_parent_categories/',views.show_parent_categories,name='show_parent_categories'),
    path('delete_parent_categories/<int:id>/',views.delete_parent_categories,name='delete_parent_categories'),
    path('export_brand/',views.export_to_csv,name='export_brand'),
    path('data_export/',views.export_to_csv,name='data_export'),
    path('CreateProduct/',views.CreateProduct,name='create_product'),
    path('UpdateProduct/<int:id>/',views.UpdateProduct,name='update_product'),
    path('DeleteProduct/<int:id>/',views.DeleteProduct,name='delete_product'),
    path('stock/',views.show_products_table,name='products_table'),
    path('dashboard/',views.show_dashboard,name='dashboard'),
    path('reports/',views.show_reports,name='reports'),
    path('store/', views.show_stores, name='show_stores'),
    path('CreateSupplier/',views.CreateSupplier,name='create supplier'),

    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('', views.product_list, name='product_list'),



]
