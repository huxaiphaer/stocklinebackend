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

YES = 'Yes'

INBOUND_OUTBOUND = [
    ('Yes', 'Yes'),
    ('No', 'No')
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
    quantity = models.FloatField(
        _('Quantity'), blank=True, null=True, default=0.0)
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

    notifications = models.BooleanField(_('Notifications'), default=False)
    user = models.ForeignKey(User, related_name='prealert', null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(_('Status'), max_length=100,
                              choices=WEIGH_BRIDGE_STATUS,
                              default=WEIGH_STATUS_DEFAULT, )
    priority = models.CharField(_('Priority'), max_length=100, choices=STATUSES,
                                default=HIGH, )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer} {self.quantity} {self.user}'

    @property
    def calculated_weight(self):
        if self.quantity:
            return self.quantity * self.packaging.quantity
        return 0


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
    account_id = models.CharField(
        _('Account ID'), max_length=400, blank=True, null=True)
    commodity = models.ForeignKey(Product,
                                  related_name='commodity_weigh_bridge',
                                  null=True, on_delete=models.SET_NULL)
    time = models.TimeField(_('Exit Time'), blank=True, null=True)
    trailer_reg_num = models.CharField(_('Trailer Registration Number'),
                                       max_length=400, blank=True, null=True)
    user = models.ForeignKey(User, related_name='weighbridge', null=True,
                             on_delete=models.SET_NULL)
    entry_date = models.DateField(_('Entry Date'), blank=True, null=True)
    exit_time = models.TimeField(_('Exit Time'), blank=True, null=True)
    print_date = models.DateField(_('Print Date'), blank=True, null=True)
    _import = models.CharField(
        _('Inbound'),
        choices=INBOUND_OUTBOUND,
        default=YES,
        max_length=400,)
    _export = models.CharField(
        _('Outbound'),
        choices=INBOUND_OUTBOUND,
        default=YES,
        max_length=400)
    client_name_field = models.ForeignKey(
        User, related_name='client_name_weight', null=True,
        on_delete=models.SET_NULL)
    from_destination = models.CharField(
        _('From'), max_length=400, blank=True, null=True)
    to_destination = models.CharField(
        _('To'), max_length=400, blank=True, null=True)
    first_weight = models.FloatField(
        _('First Weight'), max_length=400, blank=True, null=True)
    second_name = models.FloatField(
        _('Second Weight'), max_length=400, blank=True, null=True)
    net_weight = models.FloatField(
        _('Net Weight'), max_length=400, blank=True, null=True)
    # status = models.CharField(_('Status'), max_length=100,
    #                           choices=WEIGH_BRIDGE_STATUS,
    #                           default=WEIGH_STATUS_DEFAULT, )

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

    class Meta:
        verbose_name = 'Holding certificate'
        verbose_name_plural = 'Holding certificate'


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
    client_name_field = models.ForeignKey(
        User, related_name='client_name_store',
        null=True, on_delete=models.SET_NULL)
    flux = models.CharField(_('Flux'), max_length=100,
                            choices=STORE_ENTRANCE_STATUS,
                            default=WEIGH_STATUS_DEFAULT)
    type_of_management = models.CharField(
        _('Type of Management'), max_length=400, blank=True, null=True)
    store = models.CharField(
        _('Store'), max_length=400, blank=True, null=True)
    country_of_origin = CountryField()
    po_number = models.CharField(
        _('PO NUmber'), max_length=400, blank=True, null=True)
    shipment_number = models.CharField(
        _('Ship Number'), max_length=400, blank=True, null=True)
    number_of_batch = models.IntegerField(
        _('Number of batch'), blank=True, null=True)
    entry_date = models.DateField(
        _('Entry Date'), blank=True, null=True)
    quantity = models.FloatField(_('Quantity'), blank=True, null=True)
    user = models.ForeignKey(User, related_name='store_entrance', null=True,
                             on_delete=models.SET_NULL)
    client_reference = models.CharField(
        _('Client Reference'), max_length=400, blank=True, null=True)
    contract_number = models.CharField(
        _('Contract Number'), max_length=400, blank=True, null=True)
    packaging = models.ForeignKey(Packaging,
                                  related_name='packaging_store_entrance',
                                  null=True, on_delete=models.SET_NULL)

    # TODO: add calculated field : Theoretical Weight  = quantity x quantity
    #  quantity pledged.

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Store Entrance'
        verbose_name_plural = 'Store Entrance'


class CarrierStoreEntrance(TimeStampedModel, models.Model):
    """Store entrance carrier."""

    carrier_identifier = models.CharField(
        _('Carrier Identifier'), max_length=400, blank=True, null=True)
    container_number = models.CharField(
        _('Container Number'), max_length=400, blank=True, null=True)
    registration_number = models.CharField(
        _('Registration Number'), max_length=400, blank=True, null=True)
    carrier_type = models.CharField(
        _('Carrier Type'), max_length=400, blank=True, null=True)
    entry_slip_number = models.CharField(
        _('Entry slip Number'), max_length=400, blank=True, null=True)
    licence_number = models.CharField(
        _('Licence Number'), max_length=400, blank=True, null=True)
    trailer_number = models.CharField(
        _('Trailer Number'), max_length=400, blank=True, null=True)
    supervisor_name = models.CharField(
        _('Supervisor Name'), max_length=400, blank=True, null=True)
    product_entry_date = models.DateField(
        _('Product Entry Date'), blank=True, null=True)
    guardian_name = models.CharField(
        _('Guardian Name'), max_length=400, blank=True, null=True)
    comments = models.TextField(
        _('Comments'), max_length=400, blank=True, null=True)
    store_entrance = models.ForeignKey(
        StoreEntrance,
        related_name='store_entrance_carrier',
        null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}'


class ProductStoreEntrance(TimeStampedModel, models.Model):
    """Product Store Entrance"""

    purchase_order_number = models.CharField(
        _('Purchase order number'), max_length=400, blank=True, null=True)
    shipment_number = models.CharField(
        _('Shipment  number'), max_length=400, blank=True, null=True)
    batch_number = models.CharField(
        _('Batch  number'), max_length=400, blank=True, null=True)
    compliance = models.CharField(
        _('Compliance'), max_length=400, blank=True, null=True)
    amount = models.FloatField(
        _('Amount'), max_length=400, blank=True, null=True)
    grade = models.CharField(
        _('Grade'), max_length=400, blank=True, null=True)
    mark = models.CharField(
        _('Mark'), max_length=400, blank=True, null=True)
    packaging = models.ForeignKey(
        Packaging, related_name='packaging_store_entrance_product',
        null=True, on_delete=models.SET_NULL)
    theoretical_weight = models.IntegerField(
        _('Theoretical Weight'), blank=True, null=True)
    actual_weight = models.IntegerField(
        _('Actual Weight'), blank=True, null=True)
    zone_warehouse = models.FloatField(
        _('Zone warehouse'), max_length=400, blank=True, null=True)
    product_comments = models.CharField(
        _('Product Comments'), max_length=400, blank=True, null=True)
    store_entrance = models.ForeignKey(
        StoreEntrance,
        related_name='store_entrance_entrance',
        null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}'


class WareHouse(TimeStampedModel, models.Model):

    """WareHosue Model."""

    name = models.CharField(
        _('Ware House Name '), max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Season(TimeStampedModel, models.Model):

    """Season Model."""

    name = models.CharField(
        _('Season'), max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Entity(TimeStampedModel, models.Model):

    """Entity Model."""

    name = models.CharField(
        _('Entity'), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class HousingCertificateSearchModel(TimeStampedModel, models.Model):
    """HousingCertificate Model"""

    customer = models.ForeignKey(Customer,
                                 related_name='customer_hcm',
                                 null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,
                                related_name='product_hcm',
                                null=True, on_delete=models.SET_NULL)
    ware = models.ManyToManyField(WareHouse)
    season = models.ManyToManyField(Season)
    entity = models.ManyToManyField(Entity)

    def __str__(self):
        return f'{self.id}'


class ManagementByLot(TimeStampedModel, models.Model):
    """Management by lot."""

    transaction_type = models.CharField(_('Transaction Type'),
                                        max_length=100,
                                        choices=TRANSACTION_TYPES,
                                        default=DEFAULT_TRANSACTION_TYPE, )
    product = models.ForeignKey(Product, related_name='product_lot',
                                null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, related_name='customer_lot',
                                 null=True, on_delete=models.SET_NULL)
    batch_number = models.CharField(_('Batch Number '),
                                    max_length=400, blank=True, null=True)
    quantity = models.FloatField(
        _('Quantity'), blank=True, null=True, default=0.0)
    packaging = models.ForeignKey(Packaging,
                                  related_name='packaging_lot',
                                  null=True, on_delete=models.SET_NULL)
    real_weight = models.FloatField(
        _('Real weight '), blank=True, null=True, default=0.0)
    quantity_hc = models.FloatField(
        _('Quantity HC'), blank=True, null=True, default=0.0)

    def __str__(self):
        return f'{self.id}'

    @property
    def theoretical_weight(self):
        return self.packaging.quantity * self.quantity

    @property
    def theoretical_weight_hc(self):
        return self.packaging.quantity * self.quantity_hc

    @property
    def real_weight_hc(self):
        return 0