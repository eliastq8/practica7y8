from rest_framework import serializers
from .models import Fruta, Queso

class FrutaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Fruta
        fields='__all__'
        
class QuesoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Queso
        fields='__all__'