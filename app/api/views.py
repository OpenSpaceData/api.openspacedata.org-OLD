from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from api.models import Application, Indice, Satellite, Band
from api.serializers import OsdSerializer
import logging
logger = logging.getLogger(__name__)

class OsdView(APIView):
    def get(self, request):
        applications = Application.objects.all()
        serializer = OsdSerializer(applications, many=True)
        return Response({"Applications:": serializer.data})

class DetailView(APIView):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["date_from"] = self.request.query_params.get("from", None)
        print(context)
        return context

    def get(self, request, machine_name):
        application = Application.objects.get(machine_name=machine_name)
        serializer = OsdSerializer(application, context={"date_from": request.query_params.get("from", None), "date_to": request.query_params.get("to", None), "location": request.query_params.get("location", None), })

        return Response({"Everything you need to analyzing "+application.name: serializer.data})