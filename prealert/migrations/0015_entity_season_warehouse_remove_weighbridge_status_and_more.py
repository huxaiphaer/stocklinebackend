# Generated by Django 4.0.3 on 2022-10-03 10:43

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prealert', '0014_managementbylot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Entity')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Season')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Ware House Name ')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='weighbridge',
            name='status',
        ),
        migrations.RemoveField(
            model_name='housingcertificatesearchmodel',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='housingcertificatesearchmodel',
            name='season',
        ),
        migrations.RemoveField(
            model_name='housingcertificatesearchmodel',
            name='ware',
        ),
        migrations.AlterField(
            model_name='weighbridge',
            name='_export',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Outbound'),
        ),
        migrations.AlterField(
            model_name='weighbridge',
            name='_import',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Inbound'),
        ),
        migrations.AlterField(
            model_name='weighbridge',
            name='second_name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Second Weight'),
        ),
        migrations.AddField(
            model_name='housingcertificatesearchmodel',
            name='entity',
            field=models.ManyToManyField(to='prealert.entity'),
        ),
        migrations.AddField(
            model_name='housingcertificatesearchmodel',
            name='season',
            field=models.ManyToManyField(to='prealert.season'),
        ),
        migrations.AddField(
            model_name='housingcertificatesearchmodel',
            name='ware',
            field=models.ManyToManyField(to='prealert.warehouse'),
        ),
    ]
