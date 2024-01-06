from rest_framework import serializers
from Wydatki.models import Wydatki


class WydatkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wydatki
        fields = '__all__'
