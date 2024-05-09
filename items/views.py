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

    # def post(self, request):
    #     serializer = serializers.ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         item_obj = serializer.save()
    #         item_obj_serializer = serializers.ItemSerializer(item_obj)

    #         return Response(item_obj_serializer.data)
    #     else:
    #         print("serializer error!!!!")
    #         print(serializer.errors)
    #         return Response(serializer.errors)

    def post(self, request):
        item_data_list = request.data
        response_data = []

        for item_data in item_data_list:
            item_data_copy = item_data.copy()
            serializer = serializers.ItemSerializer(data=item_data_copy)

            if serializer.is_valid():
                item_obj = serializer.save()
                item_obj_serializer = serializers.ItemSerializer(item_obj)
                response_data.append(item_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error item data:", item_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)
