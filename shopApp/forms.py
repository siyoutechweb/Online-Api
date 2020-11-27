from django import forms
from .models import *
from orders.models import *

##########
class GroupSaleForm(forms.ModelForm):
    class Meta:
        model=GroupSale
        fields='__all__'

    # raising error if end_date < start_date
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")

class CreateSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
#########categry form########
class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','slug']
#############################
##########

class CreateProductForm(forms.ModelForm):
    sold_count = forms.IntegerField(required=False,initial=0)
    # store=forms.many(required=False)

    class Meta:
        model = Product
        fields = '__all__'

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CreateSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
class CreateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name','slug']

OBJECTS_CHOICES = [
('Brand', 'Brand',),
('ParentCategory', 'ParentCategory',),
('Category', 'Category',),
('Store', 'Store',),
('Product', 'Product',),
('Order', 'Order',),
('OrderItem', 'OrderItem',),
]
class ExportDataForm(forms.Form):
    class_to_export = forms.ChoiceField(label='Ready to Export',choices=OBJECTS_CHOICES,required=True)

class CreateParentCategoryForm(forms.ModelForm):
    class Meta:
        model = ParentCategory
        fields = ['name','slug']
