from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import Trait


# Create your views here.
class Traits(APIView):
    def get(self, request):
        traits = Trait.objects.all()
        serializer = serializers.TraitSerializer(
            traits,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        trait_data_list = request.data
        response_data = []

        for trait_data in trait_data_list:
            trait_data_copy = trait_data.copy()
            serializer = serializers.TraitSerializer(data=trait_data_copy)

            if serializer.is_valid():
                trait_obj = serializer.save()
                trait_obj_serializer = serializers.TraitSerializer(trait_obj)
                response_data.append(trait_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error trait data:", trait_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)
