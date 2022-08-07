"""Serializers"""
from rest_framework import serializers

from customer.models import Customer, Product, Packaging


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'customer_name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name',)


class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = ('uuid', 'packaging_name', 'packaging_type', 'quantity',
                  'packaging_capacity')
