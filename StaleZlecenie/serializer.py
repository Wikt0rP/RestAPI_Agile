from rest_framework import serializers
from StaleZlecenie.models import StaleZlecenie


class StaleZleceniaSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaleZlecenie
        fields = '__all__'
