# Generated by Django 4.0.3 on 2022-10-14 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0021_remove_season_name_season_description_season_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Entity', 'verbose_name_plural': 'Entities'},
        ),
        migrations.AlterModelOptions(
            name='factories',
            options={'verbose_name': 'Factory', 'verbose_name_plural': 'Factories'},
        ),
        migrations.RemoveField(
            model_name='productstoreentrance',
            name='store_entrance',
        ),
        migrations.AddField(
            model_name='productstoreentrance',
            name='carrier_store_entrance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrier_s_product', to='prealert.carrierstoreentrance'),
        ),
    ]