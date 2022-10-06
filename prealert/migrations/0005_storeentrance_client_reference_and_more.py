# Generated by Django 4.0.3 on 2022-09-23 17:26

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0004_alter_prealert_options_weighbridge__export_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeentrance',
            name='client_reference',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Client Reference'),
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='contract_number',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Contract Number'),
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='country_of_origin',
            field=django_countries.fields.CountryField(default='UG', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='entry_date',
            field=models.DateField(blank=True, null=True, verbose_name='Entry Date'),
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='number_of_batch',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of batch'),
        ),
        migrations.AddField(
            model_name='storeentrance',
            name='type_of_management',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Type of Management'),
        ),
    ]
