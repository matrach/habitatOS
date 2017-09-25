from rest_framework import serializers
from habitat.sensors.models import ZWaveSensor


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZWaveSensor
        fields = ['device', 'datetime', 'type', 'value', 'unit']
