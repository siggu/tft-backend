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

    def post(self, request):
        augment_data_list = request.data
        response_data = []

        for augment_data in augment_data_list:
            augment_data_copy = augment_data.copy()
            serializer = serializers.AugmentSerializer(data=augment_data_copy)

            if serializer.is_valid():
                augment_obj = serializer.save()
                augment_obj_serializer = serializers.AugmentSerializer(augment_obj)
                response_data.append(augment_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error augment data:", augment_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)
