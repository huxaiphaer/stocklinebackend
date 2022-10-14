from django.contrib import admin

from customer.models import Customer, Product, Packaging, Transport


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'ware_house', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'management_type', 'ware_house',)


class PackagingAdmin(admin.ModelAdmin):
    list_display = ('id', 'packaging_name',
                    'packaging_type', 'quantity')


class TransportAdmin(admin.ModelAdmin):
    list_display = ('description', 'phone', 'email', 'contact',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.register(Transport, TransportAdmin)
