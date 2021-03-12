from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Application, Indice, Satellite, Band
from api.serializers import ApiSerializer

class ApiView(APIView):
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApiSerializer(applications, many=True)
        return Response({"application": serializer.data})