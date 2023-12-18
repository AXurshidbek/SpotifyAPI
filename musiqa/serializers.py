from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import *

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qoshiq
        fields='__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Albom
        fields='__all__'

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qoshiqchi
        fields='__all__'
