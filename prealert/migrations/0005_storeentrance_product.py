# Generated by Django 4.0.3 on 2022-08-07 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('prealert', '0004_prealert_customer_prealert_packaging_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeentrance',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_store_entrance', to='customer.product'),
        ),
    ]
