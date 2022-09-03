from django.contrib import admin

from customer.models import Customer, Product, Packaging


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'customer_name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'product_name',)


class PackagingAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'packaging_name',
                    'packaging_type', 'quantity')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Packaging, PackagingAdmin)
