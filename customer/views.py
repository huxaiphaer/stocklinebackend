from django.shortcuts import render
from rest_framework import generics, response, status

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


class PackagingDetail(generics.ListAPIView):

    """Get packaging by product id"""
    serializer_class = PackagingSerializer

    def get(self, request, *args, **kwargs):

        """Get packaging by product ID."""
        try:
            product = Product.objects.get(id=kwargs.get("id"))
            packaging = Packaging.objects.filter(packaging_name=product)
            serializer = self.get_serializer(packaging, many=True)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return response.Response({"message": "No packaging's available"},
                                     status=status.HTTP_404_NOT_FOUND)
