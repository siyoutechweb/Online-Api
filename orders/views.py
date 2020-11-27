from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm, OrderItemCreateForm
from .models import Order
from cart.cart import Cart
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from .filters import OrderFilter
from shopApp.models import Product
from django.contrib.auth.decorators import login_required
from typing import List
from shopApp.models import *


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.fields['profile']=request.user.profile
            # form.cleaned_data['profile'] = request.user.profile.id
            # print('======================')
            # print(form)
            order = form.save()
            for item in cart:
                #productitem=item['product'].store
                #print(item['product'].update_qty(item['quantity']))
                OrderItem.objects.create(order=order,
                                    product=item['product'],
                                    price=item['price'],
                                    quantity=item['quantity'],store=item['product'].store,discount_amount=item['discount_amount'])
                s=Store.objects.filter(name=item['product'].store)
                orders_count=s[0].orders_count
                orders_count=orders_count+item['quantity']
                s.update(orders_count=orders_count)
            cart.clear()
            orderitems=OrderItem.objects.filter(order=order)
            context={'order': order,'orderitems':orderitems}
            return render(request,'shopApp/created_order.html',context)


            # clear the cart

    else:
        form = OrderCreateForm()
    return render(request,
                  'shopApp/create_order.html',
                  {'cart': cart, 'form': form})
@login_required
def show_orders(request):
    orders = OrderItem.objects.filter(store=request.user.profile.store)
    products=Product.objects.filter(store=request.user.profile.store)
    qty_warning=[]
    for product in products:
        if product.qty<= product.warn_qty:
            qty_warning.append(product)


    myFilter=OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs


    context={'orders':orders,'myFilter':myFilter,'qty_warning':len(qty_warning)}
    return render(request,'shopApp/orders_list.html',context)







@login_required
def show_my_orders(request):
    orders = Order.objects.filter(profile=request.user.profile)
    list =[]
    for o in orders:

        OItems=OrderItem.objects.filter(order=o)
        list.append(OItems[0])



    # entry_list = list(orders)

    # [scalar * num for num in vector]


    # print('===========')
    # print(list)
    context={'orders':list}
    return render(request,'shopApp/my_orders_list.html',context)











def CreateOrderItem(request):
    form = OrderItemCreateForm()
    if request.method == 'POST':
        form = OrderItemCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shopApp/orders_list.html')
    context = {'form':form}
    return render(request,'shopApp/OrderItemForm.html',context)


def UpdateOrderItem(request, id):
    orderitem = OrderItem.objects.get(id=id)
    form=OrderItemCreateForm(instance=orderitem)
    order=orderitem.order


    if request.method == 'POST':
        form = OrderItemCreateForm(request.POST, instance=orderitem)
        #print(orderitem.approved)
        if form.is_valid() and orderitem.approved:

             #
             # print('****'+str(p[0].update_qty(orderitem.quantity)))
             # print('****'+str(orderitem.quantity))
             # print('QTY1'+str(p[0].qty)+'-'+str(orderitem.quantity))
             # p[0].qty=-10
             # p[0].save()
             # print('QTY2'+str(p[0].qty))

            p=Product.objects.filter(id=orderitem.product.id)
            old_qty=p[0].qty
            new_qty=old_qty-orderitem.quantity
            if (new_qty>0):

                p=Product.objects.filter(id=orderitem.product.id).update(qty=new_qty,sold_count=+orderitem.quantity)
                form.save()
                return redirect('orders:show_orders')

    context = {'form':form,'order':order,'orderitem':orderitem}
    return render(request,'shopApp/OrderItemForm.html',context)
