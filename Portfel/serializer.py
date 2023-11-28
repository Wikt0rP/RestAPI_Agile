from rest_framework import serializers

from Portfel.models import Portfel


class PortfelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfel
        fields = '__all__'