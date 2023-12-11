from rest_framework import serializers
from StaleZlecenie.models import StaleZlecenie


class StaleZlecenieSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaleZlecenie
        fields = '__all__'
