from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('CreateOrderItem/',views.CreateOrderItem,name='create_order_item'),
    path('UpdateOrderItem/<int:id>/',views.UpdateOrderItem,name='update_order_item'),
    path('create/', views.order_create, name='order_create'),
    path('list/', views.show_orders, name='show_orders'),
    path('mylist/', views.show_my_orders, name='show_my_orders'),
]
