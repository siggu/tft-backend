from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Augment


# Create your views here.
class Augments(APIView):
    def get(self, request):
        augments = Augment.objects.all()
        serializer = serializers.AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)


class SilverAugments(APIView):
    def get(self, request):
        augments = Augment.objects.filter(tier="silver")
        serializer = serializers.AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)


class GoldAugments(APIView):
    def get(self, request):
        augments = Augment.objects.filter(tier="gold")
        serializer = serializers.AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)


class PrismaticAugments(APIView):
    def get(self, request):
        augments = Augment.objects.filter(tier="prismatic")
        serializer = serializers.AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)
