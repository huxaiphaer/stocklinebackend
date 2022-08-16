from rest_framework import serializers

from customer.models import Customer, Product, Packaging
from customer.serializers import (
    CustomerSerializer,
    ProductSerializer,
    PackagingSerializer
)
from prealert.models import PreAlert
from users.serializers import UserProfile


class PreAlertSerializer(serializers.ModelSerializer):
    user = UserProfile(read_only=True)
    customer = CustomerSerializer()
    product = ProductSerializer()
    packaging = PackagingSerializer()

    class Meta:
        model = PreAlert
        fields = (
            'uuid', 'customer', 'product', 'quantity', 'packaging',
            'weight', 'user', 'priority')

    def create(self, validated_data):
        """Save pre-alert"""

        customer = validated_data.pop('customer', {})
        product = validated_data.pop('product', {})
        packaging = validated_data.pop('packaging', {})

        print("== ", self.context['request'].user)
        pre_alert = PreAlert.objects.create(**validated_data,
                                            user=self.context['request'].user)

        if customer:
            customer_obj = Customer.objects.get(id=customer['id'])
            pre_alert.customer = customer_obj
            pre_alert.save()

        if product:
            product_obj = Product.objects.get(id=product['id'])
            pre_alert.product = product_obj
            pre_alert.save()

        if packaging:
            packaging_obj = Packaging.object.get(id=packaging['id'])
            pre_alert.packaging = packaging_obj
            pre_alert.save()

        return pre_alert
