from rest_framework import serializers

import CeleOszczednosciowe
from CeleOszczednosciowe.models import CeleOszczednosciowe


class CeleOszczednoscioweSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeleOszczednosciowe
        fields = '__all__'

