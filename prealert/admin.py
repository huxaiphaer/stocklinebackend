from django.contrib import admin

from prealert.models import PreAlert, WeighBridge, GuaranteedGoods, \
    StoreEntrance, CarrierStoreEntrance, ProductStoreEntrance


class PreAlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product',
                    'quantity', 'contract_number', 'from_or_origin',
                    'packaging', 'commentaries', 'type', 'calculated_weight',
                    'notifications', 'user', 'status', 'priority')
    readonly_fields = ('calculated_weight', )
    search_fields = ('customer__customer_name', 'contract_number',)


class WeighBridgeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'vehicle_number', 'transporter',
        'vehicle_reg_num', 'commodity', 'trailer_reg_num', 'user', 'entry_date',
        'exit_time', 'print_date', 'status',
    )
    search_fields = ('vehicle_number', 'transporter',)


class GuaranteedGoodsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'batch_number', 'quantity',
        'quantity_pledged', 'theoretical_weight', 'theoretical_weight_pledged',
        'actual_weight', 'actual_weight_guaranteed',
        'priority',)
    search_fields = ('batch_number', 'quantity',)


class CarrierStoreEntranceAdmin(admin.StackedInline):
    model = CarrierStoreEntrance
    list_display = ('id', 'carrier_identifier', 'container_number',
                    'registration_number',
                    'carrier_type', 'entry_slip_number',
                    'licence_number', 'trailer_number', 'supervisor_name',
                    'product_entry_date', 'guardian_name', 'comments', ''
                    )
    search_fields = ('carrier_identifier', 'container_number',)
    extra = 1


class ProductStoreEntranceAdmin(admin.StackedInline):
    model = ProductStoreEntrance
    list_display = ('id', 'purchase_order_number',
                    'shipment_number',
                    'batch_number',
                    'compliance',
                    'amount', 'grade', 'mark', 'theoretical_weight',
                    'packaging', 'theoretical_weight', 'actual_weight',
                    'zone_warehouse',
                    'product_comments')
    extra = 1


class StoreEntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_type', 'product', 'country',
                    'client_name',
                    'flux', 'store', 'po_number', 'shipment_number',
                    'quantity', 'user', 'packaging')
    search_fields = ('transaction_type', 'product',)
    inlines = [
        CarrierStoreEntranceAdmin,
        ProductStoreEntranceAdmin
    ]


admin.site.register(PreAlert, PreAlertAdmin)
admin.site.register(WeighBridge, WeighBridgeAdmin)
admin.site.register(GuaranteedGoods, GuaranteedGoodsAdmin)
admin.site.register(StoreEntrance, StoreEntranceAdmin)
# admin.site.register(CarrierStoreEntrance)
