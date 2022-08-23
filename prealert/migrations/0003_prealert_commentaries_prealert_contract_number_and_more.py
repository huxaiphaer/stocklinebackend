# Generated by Django 4.0.3 on 2022-08-23 07:36

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prealert',
            name='commentaries',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaries'),
        ),
        migrations.AddField(
            model_name='prealert',
            name='contract_number',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Contract Number'),
        ),
        migrations.AddField(
            model_name='prealert',
            name='from_or_origin',
            field=django_countries.fields.CountryField(default='UG', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prealert',
            name='notifications',
            field=models.BooleanField(default=False, verbose_name='Notifications'),
        ),
        migrations.AddField(
            model_name='prealert',
            name='status',
            field=models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Finished', 'Finished')], default='Incoming', max_length=100, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='prealert',
            name='type',
            field=models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], default='Inbound', max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='prealert',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=100, verbose_name='Priority'),
        ),
    ]