from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from customer.models import Customer, Product, Packaging
from customer.serializers import (
    CustomerSerializer,
    ProductSerializer,
    PackagingSerializer
)
from prealert.models import PreAlert, WeighBridge
from users.models import User
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

        customer = self.context['request'].data.get('customer_id', None)
        product = self.context['request'].data.get('product_id', None)
        packaging = self.context['request'].data.get('packaging_id', None)
        user_uuid = self.context['request'].data.get('user_uuid', None)

        user = User.objects.get(uuid=user_uuid)

        pre_alert = PreAlert.objects.create(**validated_data,
                                            user=user)

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


class WeighBridgeSerializer(serializers.ModelSerializer):
    commodity = ProductSerializer(many=False, required=False)

    class Meta:
        model = WeighBridge
        fields = (
            'vehicle_number', 'transporter',
            'account_id', 'commodity', 'time', 'trailer_reg_num',
            'user', 'entry_date', 'exit_time', 'print_date', '_import',
            '_export', 'client_name', 'from_destination', 'to_destination',
            'first_weight', 'second_name', 'net_weight', 'status',)
