from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Portal

# Create your views here.


class Portals(APIView):
    def get(self, request):
        portals = Portal.objects.all()
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        portal_data_list = request.data
        response_data = []

        for portal_data in portal_data_list:
            portal_data_copy = portal_data.copy()
            serializer = serializers.PortalSerializer(data=portal_data_copy)

            if serializer.is_valid():
                portal_obj = serializer.save()
                portal_obj_serializer = serializers.PortalSerializer(portal_obj)
                response_data.append(portal_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error portal data:", portal_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)
