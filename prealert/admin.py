from django.contrib import admin

from prealert.models import PreAlert, WeighBridge, GuaranteedGoods, \
    StoreEntrance


class PreAlertAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'quantity', 'contract_number', 'from_or_origin',
                    'commentaries', 'type', 'weight',
                    'notifications', 'status', 'priority')
    search_fields = ('customer', 'contract_number',)


class WeighBridgeAdmin(admin.ModelAdmin):
    pass


class GuaranteedGoodsAdmin(admin.ModelAdmin):
    pass


class StoreEntranceAdmin(admin.ModelAdmin):
    pass


admin.site.register(PreAlert, PreAlertAdmin)
admin.site.register(WeighBridge, WeighBridgeAdmin)
admin.site.register(GuaranteedGoods, WeighBridgeAdmin)
admin.site.register(StoreEntrance, StoreEntranceAdmin)
