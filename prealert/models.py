import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from django_extensions.db.models import TimeStampedModel

from users.models import User

STATUSES = [
    ('High', 'High'),
    ('Low', 'Low'),
]

HIGH = 'High'


WEIGH_BRIDGE_STATUS = [
    ('Incoming', 'Incoming'),
    ('Outgoing', 'Outgoing'),
    ('Finished', 'Finished'),
]

WEIGH_STATUS_DEFAULT = 'Incoming'


STORE_ENTRANCE_STATUS = [
    ('Import', 'Import'),
    ('Export', 'Export'),
]

STORE_ENTRANCE_DEFAULT = 'Import'


class PreAlert(TimeStampedModel, models.Model):
    """Pre Alert"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    customer_name = models.CharField(_('Customer'), max_length=400,
                                     blank=True, null=True)
    product = models.CharField(_('Product'),
                               max_length=500, blank=True, null=True)
    quantity = models.FloatField(_('Quantity'), blank=True, null=True)
    packaging = models.CharField(_('Packaging'),max_length=400,
                                 blank=True, null=True)
    weight = models.FloatField(_('Weight'), blank=True, null=True)
    user = models.ForeignKey(User, related_name='prealert', null=True,
                             on_delete=models.SET_NULL)
    priority = models.CharField(_('Priority'), max_length=100, choices=STATUSES,
                                default=HIGH, )

    def __str__(self):
        return f'{self.customer_name} {self.quantity}'


class WeighBridge(TimeStampedModel, models.Model):

    """WeighBridge"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    vehicle_number = models.CharField(_('Vehicle Number'),
                                      max_length=400, blank=True,
                                      null=True)
    transporter = models.CharField(_('Transporter'), max_length=400, blank=True, null=True)
    commodity_name = models.CharField(_('Commodity Name'), max_length=400,
                                      blank=True, null=True)
    vehicle_reg_num = models.CharField(_('Vehicle Registration Number'),
                                       max_length=400, blank=True, null=True)
    commodity_id = models.CharField(_('Commodity ID'), max_length=400,
                                    blank=True, null=True)
    trailer_reg_num = models.CharField(_('Trailer Registration Number'),
                                       max_length=400, blank=True, null=True)
    user = models.ForeignKey(User, related_name='weighbrifge', null=True,
                             on_delete=models.SET_NULL)
    entry_date = models.DateField(_('Entry Date'), blank=True, null=True)
    exit_time = models.TimeField(_('Exit Time'), blank=True, null=True)
    print_date = models.DateField(_('Print Date'), blank=True, null=True)
    status = models.CharField(_('Status'), max_length=100,
                              choices=WEIGH_BRIDGE_STATUS,
                              default=WEIGH_STATUS_DEFAULT, )

    def __str__(self):
        return f'{self.commodity_name}'


class GuaranteedGoods(TimeStampedModel, models.Model):

    """Guaranteed Goods."""

    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    batch_number = models.CharField(_('Batch Number '),
                                    max_length=400, blank=True, null=True)
    quantity = models.IntegerField(_('Quantity'), blank=True, null=True)
    quantity_pledged = models.IntegerField(
        _('Quantity Pledged'), blank=True, null=True)
    theoretical_weight = models.IntegerField(
        _('Theoretical Weight'), blank=True, null=True)
    theoretical_weight_pledged = models.IntegerField(
        _('Theoretical Weight Pledged'), blank=True, null=True)
    actual_weight = models.IntegerField(
        _('Actual Weight'), blank=True, null=True)
    actual_weight_guaranteed = models.IntegerField(
        _('Actual Weight Guaranteed'), blank=True, null=True)
    priority = models.CharField(_('Priority'), max_length=100,
                                choices=WEIGH_BRIDGE_STATUS,
                                default=WEIGH_STATUS_DEFAULT, )

    def __str__(self):
        return f'{self.batch_number}'


class StoreEntrance(TimeStampedModel, models.Model):

    """Store Entrance"""
    transaction_type = models.CharField(_('Transaction Type'),
                                        max_length=400, blank=True, null=True)
    product = models.IntegerField(_('Product'), blank=True, null=True)
    country = CountryField()
    client_name = models.CharField(
        _('Client Name'), max_length=400, blank=True, null=True)
    flux = models.CharField(_('Flux'), max_length=100,
                            choices=STORE_ENTRANCE_STATUS,
                            default=WEIGH_STATUS_DEFAULT)
    store = models.CharField(
        _('Store'), max_length=400, blank=True, null=True)
    po_number = models.CharField(
        _('PO NUmber'), max_length=400, blank=True, null=True)
    shipment_number = models.CharField(
        _('Ship Number'), max_length=400, blank=True, null=True)
    amount = models.FloatField(_('Amount'), blank=True, null=True)
    user = models.ForeignKey(User, related_name='store_entrance', null=True,
                             on_delete=models.SET_NULL)
    packaging = models.IntegerField(
        _('Packaging'), blank=True, null=True)
    theoretical_weight = models.IntegerField(
        _('Theoretical Weight'), blank=True, null=True)

    def __str__(self):
        return f'{self.transaction_type}'
