# Generated by Django 4.0.3 on 2022-08-07 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
        ('prealert', '0002_alter_guaranteedgoods_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prealert',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='prealert',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='storeentrance',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='storeentrance',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='storeentrance',
            name='product',
        ),
        migrations.RemoveField(
            model_name='storeentrance',
            name='theoretical_weight',
        ),
        migrations.RemoveField(
            model_name='weighbridge',
            name='commodity_id',
        ),
        migrations.RemoveField(
            model_name='weighbridge',
            name='commodity_name',
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='prealert',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_pre_alert', to='customer.product'),
        ),
        migrations.AlterField(
            model_name='storeentrance',
            name='transaction_type',
            field=models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], default='Inbound', max_length=100, verbose_name='Transaction Type'),
        ),
        migrations.AlterField(
            model_name='weighbridge',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='weighbridge', to=settings.AUTH_USER_MODEL),
        ),
    ]