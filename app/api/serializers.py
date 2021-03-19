from rest_framework import serializers
from . import views
from api.models import Application, Indice, Satellite, Band

class IndiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indice
        fields = ['name', 'accr', 'description', 'is_NormalizedDifference', 'calc', ]

class SatelliteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Satellite
        fields = ['name', 'accr', 'operator', ]

class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = ['band', 'description', 'wavelength', 'resolution', ]

class OsdSerializer(serializers.ModelSerializer):
    bands = BandSerializer(source='indice_to_use.needed_bands', many=True)
    satellite = SatelliteSerializer(source='indice_to_use.satellite_to_use')
    indice = IndiceSerializer(source='indice_to_use')

    class Meta:
        model = Application
        fields = ['machine_name', 'name', 'description', 'indice', 'satellite', 'bands', ]