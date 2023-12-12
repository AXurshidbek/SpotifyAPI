from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import *

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        meta=Qoshiq
        fields='__all__'

