from rest_framework import serializers
from habitat.sensors.models import ZWaveSensor


class ZWaveSensorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ZWaveSensor
        fields = '__all__'
