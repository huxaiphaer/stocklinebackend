from django.shortcuts import render
from rest_framework import generics

from customer.models import Customer, Product, Packaging
from customer.serializers import CustomerSerializer, ProductSerializer, \
    PackagingSerializer


class CustomerView(generics.ListCreateAPIView):
    """
    List Create Customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductView(generics.ListCreateAPIView):
    """List Create Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PackagingView(generics.ListCreateAPIView):
    """List create Packaging."""
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer
