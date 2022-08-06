from django.contrib import admin

from prealert.models import PreAlert, WeighBridge, GuaranteedGoods, \
    StoreEntrance


class PreAlertAdmin(admin.ModelAdmin):
    pass


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
