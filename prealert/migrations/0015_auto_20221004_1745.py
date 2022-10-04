# Generated by Django 4.0.3 on 2022-10-04 17:45

from django.db import migrations


class Migration(migrations.Migration):

    def gen_field(apps, schema_editor):
        MyModel = apps.get_model('prealert', 'WeighBridge')
        for row in MyModel.objects.all():
            row.from_destination = 'UG'
            row.to_destination = 'UG'
            row.save()

    dependencies = [
        ('prealert', '0014_auto_20221004_1720'),
    ]

    operations = [
        migrations.RunPython(gen_field, reverse_code=migrations.RunPython.noop),
    ]