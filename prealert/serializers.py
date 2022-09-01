from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from customer.models import Customer, Product, Packaging
from customer.serializers import (
    CustomerSerializer,
    ProductSerializer,
    PackagingSerializer
)
from prealert.models import PreAlert
from users.serializers import UserProfile


class PreAlertSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user = UserProfile(read_only=True)
    customer = CustomerSerializer(many=False, required=False)
    product = ProductSerializer(many=False, required=False)
    packaging = PackagingSerializer(many=False, required=False)

    class Meta:
        model = PreAlert
        fields = (
            'id', 'uuid', 'customer', 'product', 'quantity', 'packaging',
            'weight', 'user', 'priority', 'contract_number', 'from_or_origin',
            'commentaries', 'type', 'notifications', 'status', )

    def create(self, validated_data):
        """Save pre-alert"""

        print(" self.context['request'] ", self.context['request'].data)

        customer = self.context['request'].data.get('customer_id', None)
        product = self.context['request'].data.get('product_id', None)
        packaging = self.context['request'].data.get('packaging_id', None)

        pre_alert = PreAlert.objects.create(**validated_data,
                                            user=self.context['request'].user)

        if customer:
            customer_obj = Customer.objects.get(id=customer)
            pre_alert.customer = customer_obj
            pre_alert.save()

        if product:
            product_obj = Product.objects.get(id=product)
            pre_alert.product = product_obj
            pre_alert.save()

        if packaging:
            packaging_obj = Packaging.objects.get(id=packaging)
            pre_alert.packaging = packaging_obj
            pre_alert.save()

        return pre_alert
