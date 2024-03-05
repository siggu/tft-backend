from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Origin, Job


# Create your views here.
class Origins(APIView):
    def get(self, reqeust):
        origins = Origin.objects.all()
        serializer = serializers.OriginSerializer(
            origins,
            many=True,
        )
        return Response(serializer.data)


class Jobs(APIView):
    def get(self, reqeust):
        origins = Job.objects.all()
        serializer = serializers.JobSerializer(
            origins,
            many=True,
        )
        return Response(serializer.data)
