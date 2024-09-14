from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Set12Charm

# Create your views here.

class Set12Charms(APIView):
    def get(self, request):
        charms = Set12Charm.objects.all()
        serializer = serializers.Set12CharmSerializer(
            charms,
            many=True,
        )
        return Response(serializer.data)
    
    def post(self, request):
        charm_data_list = request.data
        response_data = []
        
        for charm_data in charm_data_list:
            charm_data_copy = charm_data.copy()
            serializer = serializers.Set12CharmSerializer(data=charm_data_copy)
            
            if serializer.is_valid():
                charm_obj = serializer.save()
                charm_obj_serializer = serializers.Set12CharmSerializer(charm_obj)
                response_data.append(charm_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error portal data:", charm_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)
                
        return Response(response_data)
    
    def delete(self, requets):
        charms = Set12Charm.objects.all()
        charms.delete()
        return Response(status=status.HTTP_200_OK)