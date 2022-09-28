from import_export import resources

from prealert import models


class PreAlertCommonResourcesClass(resources.ModelResource):
    class Meta:
        model = models.PreAlert
        fields = ('uuid', 'customer__customer_name', 'product__product_name',
                  'quantity', 'contract_number', 'from_or_origin',
                  'packaging__packaging_name', 'commentaries', 'notifications',
                  'user__email', 'status', 'priority',)


class WeighBridgeCommonResourcesClass(resources.ModelResource):
    class Meta:
        model = models.WeighBridge
        fields = ('uuid', 'vehicle_number', 'transporter',
                  'vehicle_reg_num', 'account_id', 'commodity__product_name',
                  'time', 'trailer_reg_num', 'user__email',
                  'entry_date', 'exit_time', 'print_date', '_import', '_export',
                  'client_name_field__email', 'from_destination',
                  'to_destination', 'first_weight', 'second_name', 'net_weight',
                  'status',)