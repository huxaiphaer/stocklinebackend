import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class Customer(TimeStampedModel, models.Model):
    """Customer"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    customer_name = models.CharField(_('Customer Name'), max_length=400,
                                     blank=True, null=True)

    def __str__(self):
        """Return customer name."""
        return f'{self.customer_name}'


class Product(TimeStampedModel, models.Model):
    """Product"""

    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    product_name = models.CharField(_('Product Name'), max_length=400,
                                    blank=True, null=True)

    def __str__(self):
        return f'{self.product_name}'


class Packaging(TimeStampedModel, models.Model):
    """Packaging"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    packaging_name = models.ForeignKey(Product,
                                       related_name='packaging_name_package',
                                       null=True, on_delete=models.SET_NULL)
    packaging_type = models.CharField(_('Packaging Type'), max_length=400,
                                      blank=True, null=True)
    quantity = models.FloatField(_('Quantity'),
                                 blank=True, null=True)

    def __str__(self):
        return f'{self.packaging_name}'
