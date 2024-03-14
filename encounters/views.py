from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import Encounter

# Create your views here.


class Encounters(APIView):
    def get(self, request):
        encounters = Encounter.objects.all()
        serializer = serializers.EncounterSerializer(
            encounters,
            many=True,
        )
        return Response(serializer.data)
