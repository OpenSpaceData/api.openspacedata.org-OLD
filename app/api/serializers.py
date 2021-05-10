from rest_framework import serializers
from . import views
from api.models import Application, Indice, Satellite, Band
from satsearch import Search

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
    files = serializers.SerializerMethodField()
    
    def get_files(self, instance):
            bands = instance.bands

            # configuration
            url = 'https://earth-search.aws.element84.com/v0' # URL to Sentinel 2 AWS catalog
            collection = 'sentinel-s2-l2a-cogs'

            # search parameter
            startDate = '2021-04-10'
            endDate = '2021-04-12'
            location = [ 13.6677,
                    43.7232,
                    16.2605,
                    45.4522
                ]

            bbox_search = Search(
                bbox=location, 
                datetime=startDate+"/"+endDate, 
                query={'eo:cloud_cover': {'lt': 50}},
                collections=[collection],
                url=url,
                sort={'field': 'eo:cloud_cover', 'direction': 'desc'},
            )

            items = bbox_search.items()
            
            downloads = {}
            
            for i, item in enumerate(items):
                
                data = {}
                
                data['Product ID']= item.properties["sentinel:product_id"]
                data['Preview']= item.asset("thumbnail")["href"]
                data['Date']= item.properties["datetime"]
                data['Cloud cover']= item.properties["eo:cloud_cover"]
                
                for band in bands.split(','):
                    data[band] = item.asset(band)["href"]
                
                downloads[i] = data

            print(band)                        
            return downloads

    class Meta:
        model = Application
        fields = ['machine_name', 'name', 'description', 'indice', 'satellite', 'bands', 'files', ]