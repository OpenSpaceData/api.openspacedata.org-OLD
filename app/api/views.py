from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Application, Indice, Satellite, Band
from api.serializers import OsdSerializer

class OsdView(APIView):
    def get(self, request):
        applications = Application.objects.all()
        serializer = OsdSerializer(applications, many=True)
        return Response({"Your open space data:": serializer.data})