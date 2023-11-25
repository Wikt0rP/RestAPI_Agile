from rest_framework import serializers

from Grupa.models import Grupa


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grupa
        fields = '__all__'

