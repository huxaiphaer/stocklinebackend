# Generated by Django 4.0.3 on 2022-08-23 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packaging',
            name='packaging_capacity',
        ),
        migrations.AddField(
            model_name='packaging',
            name='packaging_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='packaging_name_package', to='customer.product'),
        ),
    ]