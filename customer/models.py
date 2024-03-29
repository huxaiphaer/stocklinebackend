import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

MANAGEMENT_TYPES = [
    ('Mass', 'Mass'),
    ('Lot', 'Lot'),
]

DEFAULT_TYPE = 'Mass'


class Product(TimeStampedModel, models.Model):
    """Product"""

    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    product_name = models.CharField(_('Product Name'), max_length=400,
                                    blank=True, null=True)
    management_type = models.CharField(_('Type'), max_length=100,
                                       choices=MANAGEMENT_TYPES,
                                       default=DEFAULT_TYPE, )
    ware_house = models.ForeignKey('prealert.Entity',
                                   related_name='ware_house_customer',
                                   null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product_name}'


class Customer(TimeStampedModel, models.Model):
    """Customer"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    customer_name = models.CharField(_('Customer Name'), max_length=400,
                                     blank=True, null=True)
    ware_house = models.ManyToManyField('prealert.WareHouse',
                                        related_name='ware_house_customer',
                                        null=True)

    def __str__(self):
        """Return customer name."""
        return f'{self.customer_name}'


class PackagingType(TimeStampedModel, models.Model):
    """Packaging type"""

    package_type = models.CharField(_('Package Type'), max_length=400,
                                    blank=True, null=True)

    def __str__(self):
        return f'{self.id}'


class Packaging(TimeStampedModel, models.Model):
    """Packaging"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    packaging_name = models.ForeignKey(Product,
                                       related_name='packaging_name_package',
                                       null=True, on_delete=models.SET_NULL)
    package_type = models.ForeignKey(
        PackagingType, related_name='packaging_type_pack', null=True,
        on_delete=models.SET_NULL)
    quantity = models.FloatField(_('Quantity'),
                                 blank=True, null=True)

    def __str__(self):
        return f'{self.packaging_name} {self.package_type} {self.quantity}'


class Transport(TimeStampedModel, models.Model):
    """Transporter."""
    description = models.TextField(_('Description'),
                                   blank=True, null=True)
    phone = models.CharField(
        _('Phone'), max_length=100, null=True, blank=True)
    email = models.EmailField(_('Email'))
    contact = models.CharField(
        _('Contact'), max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Transporter'
        verbose_name_plural = 'Transporters'
