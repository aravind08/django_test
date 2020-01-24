# Generated by Django 3.0.2 on 2020-01-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iotdata',
            name='battery_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='iotdata',
            name='gps_latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='iotdata',
            name='gps_longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='iotdata',
            name='pulse_counter',
            field=models.IntegerField(null=True),
        ),
    ]
