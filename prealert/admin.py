from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from import_export.admin import ImportExportMixin
from django.utils.translation import gettext_lazy as _

from customer.models import Transport
from prealert.models import PreAlert, WeighBridge, GuaranteedGoods, \
    StoreEntrance, CarrierStoreEntrance, ProductStoreEntrance, ManagementByLot, \
    WareHouse, Season, Entity, Factories
from prealert.resources import PreAlertCommonResourcesClass, \
    WeighBridgeCommonResourcesClass
from prealert.utils import ExportCsvMixin


class PreAlertAdmin(ImportExportMixin, admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id', 'customer', 'product',
                    'quantity', 'contract_number', 'from_or_origin',
                    'packaging', 'commentaries', 'type',
                    'notifications', 'user', 'status', 'priority')
    readonly_fields = ('calculated_weight',)
    fieldsets = (
        ('Pre Alert fields', {
            'fields': ('customer', 'product',
                       'quantity', 'contract_number', 'from_or_origin',
                       'packaging', 'commentaries', 'type',
                       'notifications', 'user', 'status', 'priority')
        }),
        ('Weight', {
            'fields': ('calculated_weight',)
        }),
    )
    search_fields = ('customer__customer_name', 'contract_number',)
    resource_class = PreAlertCommonResourcesClass

    actions = ["export_as_csv"]


class WeighBridgeAdmin(ImportExportMixin, admin.ModelAdmin, ExportCsvMixin):

    list_display = ('id', 'print_date', 'vehicle_number', 'entry_date',
                    'transporter', 'exit_time',
                    'vehicle_reg_num', 'trailer_reg_num',
                    'customer',
                    'commodity', 'user')
    search_fields = ('vehicle_number', 'transporter',)
    resource_class = WeighBridgeCommonResourcesClass
    exclude = ('client_name_field', )
    actions = ["export_as_csv"]


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
    list_display = ('id', 'product', 'country',
                    'client_name_field',
                    'flux', 'store', 'po_number', 'shipment_number',
                    'quantity', 'user', 'packaging')
    search_fields = ('product',)
    inlines = [
        CarrierStoreEntranceAdmin,
        ProductStoreEntranceAdmin
    ]


class ManagementByLotFilter(SimpleListFilter):

    title = _('Management by Lot')

    parameter_name = 'lot'

    def lookups(self, request, model_admin):
        return (
            ('filtered', _('filtered')),
        )

    def queryset(self, request, queryset):
        print(dir(request))
        print(request.GET.get('customer'))
        if self.value() == 'filtered':
            return queryset.filter(product__id=1, customer__id=1)


class ManagementByLotAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'customer', 'batch_number',
                    'quantity', 'real_weight')


    def get_queryset(self, request):
        qs = super(ManagementByLotAdmin, self).get_queryset(request)
        customer = request.GET.get("customer")
        product = request.GET.get("product")

        return qs.filter(product__id=product, customer__id=customer)


class WareHouseAdmin(admin.ModelAdmin):

    list_display = ('name', )


class SeasonAdmin(admin.ModelAdmin):

    list_display = ('description', )


class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', )


class FactoriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(PreAlert, PreAlertAdmin)
admin.site.register(WeighBridge, WeighBridgeAdmin)
admin.site.register(GuaranteedGoods, GuaranteedGoodsAdmin)
admin.site.register(StoreEntrance, StoreEntranceAdmin)
admin.site.register(ManagementByLot, ManagementByLotAdmin)
admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Factories, FactoriesAdmin)
