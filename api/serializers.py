from rest_framework import serializers
from shopApp.models import *


class ProdcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
