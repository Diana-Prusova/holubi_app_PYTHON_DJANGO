# api/serializers.py
from rest_framework import serializers
from mapa_holubu.models import Holubi

class HolubiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holubi
        fields = [
            'jmeno', 
            'datum', 
            'latitude', 
            'longitude', 
            'adresa', 
            'potvrzena_streba', 
            'prezil', 
            'popis'
        ]
