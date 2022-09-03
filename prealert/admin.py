from django.contrib import admin

from prealert.models import PreAlert, WeighBridge, GuaranteedGoods, \
    StoreEntrance


class PreAlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product',
                    'quantity', 'contract_number', 'from_or_origin',
                    'packaging', 'commentaries', 'type', 'weight',
                    'notifications', 'user', 'status', 'priority')
    search_fields = ('customer', 'contract_number',)


class WeighBridgeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'vehicle_number', 'transporter',
        'vehicle_reg_num', 'commodity', 'trailer_reg_num', 'user', 'entry_date',
        'exit_time', 'print_date', 'status',
    )
    search_fields = ('vehicle_number', 'transporter',)


class GuaranteedGoodsAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'batch_number', 'quantity',
        'quantity_pledged', 'theoretical_weight', 'theoretical_weight_pledged',
        'actual_weight', 'actual_weight_guaranteed',
        'priority',)
    search_fields = ('batch_number', 'quantity',)


class StoreEntranceAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'product', 'country', 'client_name',
                    'flux', 'store', 'po_number', 'shipment_number',
                    'quantity', 'user', 'packaging')
    search_fields = ('transaction_type', 'product',)


admin.site.register(PreAlert, PreAlertAdmin)
admin.site.register(WeighBridge, WeighBridgeAdmin)
admin.site.register(GuaranteedGoods, GuaranteedGoodsAdmin)
admin.site.register(StoreEntrance, StoreEntranceAdmin)
