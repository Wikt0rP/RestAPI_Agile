from rest_framework import serializers

from Skrzynka.models import Skrzynka


class SkrzynkaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skrzynka
        fields = '__all__'

