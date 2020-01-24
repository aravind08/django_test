# python imports
import re

# django imports
from django.db import models
from django.core.validators import RegexValidator

class IoTData(models.Model):
    """
    Stores the data from the box
    """
    q = models.CharField(max_length=512)
    box_number =  models.CharField(
        max_length=4,
        null=True,
        validators=[
            RegexValidator(
                regex='^[A-Z0-9]{4}$',
                message='Invalid BoxNumber',
            )
        ],
    )
    gps_latitude =  models.FloatField(null=True)
    gps_longitude =  models.FloatField(null=True)
    pulse_counter =  models.IntegerField(null=True)
    battery_level =  models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'iot_data'
        ordering = ["-created_at"]
        db_table = 'iot_data'
        verbose_name = "iot_datum"
        verbose_name_plural = "iot_data"
