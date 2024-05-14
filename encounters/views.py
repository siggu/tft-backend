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

    def post(self, request):
        encounter_data_list = request.data
        response_data = []
        for encounter_data in encounter_data_list:
            update_data = {
                "ingameKey": encounter_data.get("apiName"),
                "encounterDesc": encounter_data.get("encounterDesc"),
                "name": encounter_data.get("title"),
                "tileImageUrl": encounter_data.get("tileImageUrl"),
            }
            serializer = serializers.EncounterSerializer(data=update_data)

            if serializer.is_valid():
                encounter_obj = serializer.save()
                encounter_obj_serializer = serializers.EncounterSerializer(
                    encounter_obj
                )
                response_data.append(encounter_obj_serializer.data)
            else:
                print("serializer error!")
                print("error encounter data :", encounter_data)
                print(serializer.errors)
                response_data.append(serializer.errors)
        return Response(response_data)
