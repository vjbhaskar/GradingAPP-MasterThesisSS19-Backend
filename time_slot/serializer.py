from rest_framework import serializers
from time_slot.models import Time_Slot


class Time_SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Time_Slot
        fields = '__all__'
