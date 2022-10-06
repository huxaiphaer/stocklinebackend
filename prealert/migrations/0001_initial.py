# Generated by Django 4.0.3 on 2022-08-16 09:13

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuaranteedGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('batch_number', models.CharField(blank=True, max_length=400, null=True, verbose_name='Batch Number ')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('quantity_pledged', models.IntegerField(blank=True, null=True, verbose_name='Quantity Pledged')),
                ('theoretical_weight', models.IntegerField(blank=True, null=True, verbose_name='Theoretical Weight')),
                ('theoretical_weight_pledged', models.IntegerField(blank=True, null=True, verbose_name='Theoretical Weight Pledged')),
                ('actual_weight', models.IntegerField(blank=True, null=True, verbose_name='Actual Weight')),
                ('actual_weight_guaranteed', models.IntegerField(blank=True, null=True, verbose_name='Actual Weight Guaranteed')),
                ('priority', models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Finished', 'Finished')], default='Incoming', max_length=100, verbose_name='Priority')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.FloatField(blank=True, null=True, verbose_name='Quantity')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Weight')),
                ('priority', models.CharField(choices=[('High', 'High'), ('Low', 'Low')], default='High', max_length=100, verbose_name='Priority')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreEntrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('transaction_type', models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], default='Inbound', max_length=100, verbose_name='Transaction Type')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('client_name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Client Name')),
                ('flux', models.CharField(choices=[('Import', 'Import'), ('Export', 'Export')], default='Incoming', max_length=100, verbose_name='Flux')),
                ('store', models.CharField(blank=True, max_length=400, null=True, verbose_name='Store')),
                ('po_number', models.CharField(blank=True, max_length=400, null=True, verbose_name='PO NUmber')),
                ('shipment_number', models.CharField(blank=True, max_length=400, null=True, verbose_name='Ship Number')),
                ('quantity', models.FloatField(blank=True, null=True, verbose_name='Quantity')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeighBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=400, null=True, verbose_name='Vehicle Number')),
                ('transporter', models.CharField(blank=True, max_length=400, null=True, verbose_name='Transporter')),
                ('vehicle_reg_num', models.CharField(blank=True, max_length=400, null=True, verbose_name='Vehicle Registration Number')),
                ('trailer_reg_num', models.CharField(blank=True, max_length=400, null=True, verbose_name='Trailer Registration Number')),
                ('entry_date', models.DateField(blank=True, null=True, verbose_name='Entry Date')),
                ('exit_time', models.TimeField(blank=True, null=True, verbose_name='Exit Time')),
                ('print_date', models.DateField(blank=True, null=True, verbose_name='Print Date')),
                ('status', models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Finished', 'Finished')], default='Incoming', max_length=100, verbose_name='Status')),
                ('commodity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commodity_weigh_bridge', to='customer.product')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
