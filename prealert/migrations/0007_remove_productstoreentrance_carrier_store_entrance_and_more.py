# Generated by Django 4.0.3 on 2022-09-23 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0006_carrierstoreentrance_productstoreentrance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productstoreentrance',
            name='carrier_store_entrance',
        ),
        migrations.AddField(
            model_name='productstoreentrance',
            name='store_entrance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store_entrance_entrance', to='prealert.storeentrance'),
        ),
    ]
