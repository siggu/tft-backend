from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Item


# Create your views here.
class Items(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = serializers.ItemSerializer(
            items,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            item_obj = serializer.save()
            item_obj_serializer = serializers.ItemSerializer(item_obj)
            print
            return Response(item_obj_serializer.data)
        else:
            print("serializer error!!!!")
            print(serializer.errors)
            return Response(serializer.errors)
