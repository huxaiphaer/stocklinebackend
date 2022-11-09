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

    packaging_name = ProductSerializer(many=False, required=False)

    # TODO: packaging_type

    class Meta:
        model = Packaging
        fields = ('id', 'uuid', 'packaging_name', 'quantity',)
