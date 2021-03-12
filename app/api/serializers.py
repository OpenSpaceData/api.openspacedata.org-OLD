from rest_framework import serializers
from . import views
from api.models import Application, Indice, Satellite, Band

class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()