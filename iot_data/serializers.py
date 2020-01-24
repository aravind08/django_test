# lib imports
from rest_framework import serializers

# app level imports
from .models import IoTData
from .constants import Q_STRING_CONFIG


class IoTDataSerializer(serializers.ModelSerializer):
    q = serializers.CharField(max_length=512)

    def validate(self, data):
        q = data["q"]
        validated_data = {
            "q": q
        }
        for x in q.split('_'):
            key = x[:2]
            value = x[2:]
            if key in Q_STRING_CONFIG:
                validated_data[Q_STRING_CONFIG[key]["name"]] = value

        validated_keys = [x for x in validated_data.keys()]
        for item in [value["name"] for key, value in Q_STRING_CONFIG.items() if value["required"] is True]:
            if item not in validated_data:
                raise serializers.ValidationError("Invalid Q String")

        return validated_data

    def create(self, validated_data):
        return IoTData.objects.create(**validated_data)

    class Meta:
        model = IoTData
        fields = [
            'id',
            'box_number',
            'gps_latitude',
            'gps_longitude',
            'pulse_counter',
            'battery_level',
            'q',
            'created_at',
        ]