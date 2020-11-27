from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User
from easy_pdf.views import PDFTemplateView
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.edit import UpdateView
from .forms import *
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter
from django.core.paginator import Paginator
from orders.models import *
from decimal import *
from django.utils.translation import gettext as _
from django.utils.text import format_lazy
from django.utils import translation
import csv, io
from django.contrib import messages
from django.apps import apps

# def category_main_view(request):
#     cats=categories.objects.all()
#     catDict={'cats':cats}
#     return render(request,'shopApp/catT.html',catDict)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(available=True)
    products = Product.objects.filter(available=True)
    myFilter=ProductFilter(request.GET, queryset=products)
    products=myFilter.qs

    paginator= Paginator(products,5)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage, InvalidPage):
        products=paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shopApp/products.html',{'category': category,'categories': categories,'products': products,'myFilter':myFilter})

# def product_list3(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,'main3.html',{'category': category,'categories': categories,'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    like_count=Like.objects.filter(product=id).count()
    base_url='https://online.com:8000'
    #+product.get_absolute_url
    product_url=request.build_absolute_uri
    context={'product': product,'cart_product_form':cart_product_form,'like_count':like_count,'product_url':product_url}
    return render(request,
              'shopApp/detail.html',context)

def show_main(request):
    return render(request,'main.html')

def show_main2(request):
    return render(request,'main2.html')
def show_contact(request):
    return render(request,'contact.html')

def show_login(request):
    return render(request,'login.html')

def show_home_client(request):
    categories = Category.objects.filter(available=True)
    products = Product.objects.filter(promoted=True)
    last_sold_product=Product.objects.latest('created')
    context={'categories':categories,
    'products':products,
    'last_sold_product':last_sold_product

    }
    return render(request,'shopApp/home_client.html',context)


def show_products_table(request, category_slug=None):
    category = None
    categories = Category.objects.filter(available=True)
    products = Product.objects.filter(available=True,store=request.user.profile.store).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shopApp/products_table.html',{'category': category,'categories': categories,'products': products})

def show_dashboard(request):
    products = Product.objects.filter(available=True,store=request.user.profile.store)
    categories = Category.objects.filter(available=True)
    orderitems=OrderItem.objects.filter(store=request.user.profile.store)
    total_rev=0
    total_discount=0
    total_sold_items=0
    list_total_clients=[]

    for oi in orderitems:
        if oi.approved:
            total_rev=total_rev+oi.price*oi.quantity
            total_discount=total_discount+oi.discount_amount
            total_sold_items=total_sold_items+oi.quantity
            list_total_clients.append(oi.order.profile)
    total_clients=len(list_total_clients)

    context={
    'products':products,
    'categories':categories,
    'total_rev':total_rev,
    'orderitems_count':orderitems.count(),
    'total_discount':total_discount,
    'total_sold_items':total_sold_items,
    'total_clients':total_clients
    }
    return render(request,'shopApp/dashboard.html',context)




def show_reports(request):
    return render(request,'shopApp/reports.html')

def CreateProduct(request):
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shopApp:products_table')
    context = {'form':form}
    return render(request,'shopApp/CreateProductForm.html',context)
########create supplier####
def CreateSupplier(request):
    form = CreateSupplierForm()
    if request.method == 'POST':
        form = CreateSupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shopApp:suppliers_table')
    context = {'form':form}
    return render(request,'shopApp/CreateSupplierForm.html',context)
###########################
# def CreateComment(request, pid):
#     from =CreateCommentForm()
#     if request.method == 'POST':
#         form = CreateCommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('shopApp:products_table')
#     context = {'form':form}
#     return render(request,'shopApp/CreateProductForm.html',context)









def UpdateProduct(request, id):
    product = Product.objects.get(id=id)
    form=CreateProductForm(instance=product)


    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shopApp:products_table')



    context = {'form':form}
    return render(request,'shopApp/CreateProductForm.html',context)

def DeleteProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('shopApp:products_table')
    context={'item':product}
    return render(request,'shopApp/delete_product.html',context)


@login_required
def show_stores(request):
    stores=Store.objects.filter(name=request.user.profile.store)
    products=Product.objects.filter(store=stores[0]).order_by('-id')[:3]
    context={'stores':stores,'products':products}
    return render(request,'shopApp/show_stores.html',context)

@login_required
def add_like(request, product_id):
    exist=Like.objects.get_object_or_404(user=request.user,product=product_id)
    if exist==False:
        to_add=Like(user=request.user,product=product_id)
        to_add.save()



# Create your views here.
# one parameter named request
from .models import *
#########categry upload#########
def category_upload(request):
    if request.method == 'GET':
        categorys=Category.objects.all().order_by('-id')
        form = CreateCategoryForm()
        context = {'categorys':categorys,'form':form}
        return render(request, 'shopApp/upload_category.html', context)

    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Category.objects.update_or_create(
                #parentcategory=column[0],
                name=column[0],
                slug=column[1]
            )
        if form.is_valid():
            form.save()
            return redirect('shopApp:category_upload')

    return render(request, 'shopApp/upload_category.html', context)
################################
def brand_upload(request):
    if request.method == 'GET':
        brands=Brand.objects.all().order_by('-id')
        form = CreateBrandForm()
        context = {'brands':brands,'form':form}
        return render(request, 'shopApp/upload_brand.html', context)

    if request.method == 'POST':
        form = CreateBrandForm(request.POST)
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Brand.objects.update_or_create(
                name=column[0],
                slug=column[1]
            )
        if form.is_valid():
            form.save()
            return redirect('shopApp:brand_upload')

    return render(request, 'shopApp/upload_brand.html', context)


def export_to_csv(request):
    form=ExportDataForm()
    if request.method == 'POST':
        form=ExportDataForm(request.POST)
        models = {
            model.__name__: model for model in apps.get_models()
        }
        if form.is_valid():
            model_name=form.cleaned_data['class_to_export']
        model_class = models[model_name]
        meta = model_class._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in model_class.objects.all():
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    if request.method == 'GET':
        context={'form':form}
        return render(request, 'shopApp/data_export.html', context)




def show_parent_categories(request):
    pt=ParentCategory.objects.all().order_by('id')

    form=CreateParentCategoryForm()

    if request.method == 'POST':
        form=CreateParentCategoryForm(request.POST)
        if form.is_valid():
            form.save()

    context={'ParentCategory':pt,'form':form}
    return render(request,'shopApp/show_parent_categories.html',context)

def delete_parent_categories(request, id):
    pc = ParentCategory.objects.get(id=id)
    if request.method == 'POST':
        pc.delete()
        return redirect('shopApp:show_parent_categories')
    context={'pc':pc}
    return render(request,'shopApp/confirm_delete_parent_category.html',context)
