# Generated by Django 4.0.3 on 2022-09-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0012_housingcertificatesearchmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingcertificatesearchmodel',
            name='entity',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Entity'),
        ),
    ]
