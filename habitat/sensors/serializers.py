from rest_framework import serializers
from habitat.sensors.models import Sensor


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['location', 'value']
