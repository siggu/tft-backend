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


class ChampPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="champ")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)


class CombatPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="combat")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)


class SpatulaPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="spatula")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)


class CoinPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="coin")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)


class CardPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="card")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)


class ItemPortals(APIView):
    def get(self, request):
        portals = Portal.objects.filter(portal_type="item")
        serializer = serializers.PortalSerializer(
            portals,
            many=True,
        )
        return Response(serializer.data)
