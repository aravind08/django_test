# django imports
from django.contrib import admin

# app-level imports
from .models import IoTData

class IoTDataAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'box_number',
        'latitude',
        'longitude',
        'pulse_counter',
        'battery_level',
        'q',
    )
    ordering = ('id',)

    def latitude(self, obj):
        return obj.gps_latitude
    latitude.short_description = "latitude"


    def longitude(self, obj):
        return obj.gps_longitude
    longitude.short_description = "longitude"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

admin.site.register(IoTData, IoTDataAdmin)