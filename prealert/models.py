import uuid as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from django_extensions.db.models import TimeStampedModel

from customer.models import Product, Packaging, Customer
from users.models import User

TYPE_STATUSES = [
    ('Inbound', 'Inbound'),
    ('Outbound', 'Outbound'),
]

STATUSES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
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

TRANSACTION_TYPES = [
    ('Inbound', 'Inbound'),
    ('Outbound', 'Outbound'),
]

DEFAULT_TRANSACTION_TYPE = 'Inbound'


class PreAlert(TimeStampedModel, models.Model):
    """Pre Alert"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    customer = models.ForeignKey(Customer,
                                 related_name='customer_name_pre_alert',
                                 null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,
                                related_name='product_pre_alert',
                                null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(_('Quantity'), blank=True, null=True)
    contract_number = models.CharField(_('Contract Number'),
                                       max_length=400, blank=True,
                                       null=True)
    from_or_origin = CountryField()
    packaging = models.ForeignKey(Packaging,
                                  related_name='packaging_pre_alert',
                                  null=True, on_delete=models.SET_NULL)
    commentaries = models.TextField(_('Commentaries'), null=True, blank=True)
    type = models.CharField(_('Type'), max_length=100,
                            choices=TYPE_STATUSES,
                            default=DEFAULT_TRANSACTION_TYPE, )

    weight = models.FloatField(_('Weight'), blank=True, null=True)
    notifications = models.BooleanField(_('Notifications'), default=False)
    user = models.ForeignKey(User, related_name='prealert', null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(_('Status'), max_length=100,
                              choices=WEIGH_BRIDGE_STATUS,
                              default=WEIGH_STATUS_DEFAULT, )
    priority = models.CharField(_('Priority'), max_length=100, choices=STATUSES,
                                default=HIGH, )

    def __str__(self):
        return f'{self.customer} {self.quantity} {self.user}'


class WeighBridge(TimeStampedModel, models.Model):
    """WeighBridge"""
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    vehicle_number = models.CharField(_('Vehicle Number'),
                                      max_length=400, blank=True,
                                      null=True)
    transporter = models.CharField(_('Transporter'), max_length=400,
                                   blank=True, null=True)
    vehicle_reg_num = models.CharField(_('Vehicle Registration Number'),
                                       max_length=400, blank=True, null=True)
    commodity = models.ForeignKey(Product,
                                  related_name='commodity_weigh_bridge',
                                  null=True, on_delete=models.SET_NULL)
    trailer_reg_num = models.CharField(_('Trailer Registration Number'),
                                       max_length=400, blank=True, null=True)
    user = models.ForeignKey(User, related_name='weighbridge', null=True,
                             on_delete=models.SET_NULL)
    entry_date = models.DateField(_('Entry Date'), blank=True, null=True)
    exit_time = models.TimeField(_('Exit Time'), blank=True, null=True)
    print_date = models.DateField(_('Print Date'), blank=True, null=True)
    status = models.CharField(_('Status'), max_length=100,
                              choices=WEIGH_BRIDGE_STATUS,
                              default=WEIGH_STATUS_DEFAULT, )

    def __str__(self):
        return f'{self.uuid}  {self.vehicle_number}'


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

    # TODO: Revise the theoretical fields.
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
                                        max_length=100,
                                        choices=TRANSACTION_TYPES,
                                        default=DEFAULT_TRANSACTION_TYPE, )
    product = models.ForeignKey(Product, related_name='product_store_entrance',
                                null=True, on_delete=models.SET_NULL)
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
    quantity = models.FloatField(_('Quantity'), blank=True, null=True)
    user = models.ForeignKey(User, related_name='store_entrance', null=True,
                             on_delete=models.SET_NULL)
    packaging = models.ForeignKey(Packaging,
                                  related_name='packaging_store_entrance',
                                  null=True, on_delete=models.SET_NULL)

    # TODO: add calculated field : Theoretical Weight  = quantity x quantity
    #  quantity pledged.

    def __str__(self):
        return f'{self.id}'
