from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Comp


class Comps(APIView):
    def get(self, request):
        comps = Comp.objects.all()
        serializer = serializers.CompSerializer(
            comps,
            many=True,
        )
        return Response(serializer.data)
