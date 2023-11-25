from rest_framework import serializers

import HistoriaTransakcji
from HistoriaTransakcji.models import HistoriaTransakcji


class HistoriaTransakcjiSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoriaTransakcji
        fields = '__all__'

