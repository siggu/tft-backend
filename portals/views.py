from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Set11Portal, Set12Portal
from rest_framework import status
# Create your views here.


class Set11Portals(APIView):
    def get(self, request):
        portals = Set11Portal.objects.all()
        serializer = serializers.Set11PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        portal_data_list = request.data
        response_data = []

        for portal_data in portal_data_list:
            portal_data_copy = portal_data.copy()
            serializer = serializers.Set11PortalSerializer(data=portal_data_copy)

            if serializer.is_valid():
                portal_obj = serializer.save()
                portal_obj_serializer = serializers.Set11PortalSerializer(portal_obj)
                response_data.append(portal_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error portal data:", portal_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)

class Set12Portals(APIView):
    def get(self, request):
        portals = Set12Portal.objects.all()
        serializer = serializers.Set12PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        portal_data_list = request.data
        response_data = []

        for portal_data in portal_data_list:
            portal_data_copy = portal_data.copy()
            serializer = serializers.Set12PortalSerializer(data=portal_data_copy)

            if serializer.is_valid():
                portal_obj = serializer.save()
                portal_obj_serializer = serializers.Set12PortalSerializer(portal_obj)
                response_data.append(portal_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error portal data:", portal_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)

    def delete(self, requets):
        portals = Set12Portal.objects.all()
        portals.delete()
        return Response(status=status.HTTP_200_OK)

def make_error(request):
    division_by_zero = 1/0