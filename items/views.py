from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Item, ItemRecipe


# Create your views here.
class Items(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = serializers.ItemSerializer(
            items,
            many=True,
        )
        return Response(serializer.data)


class ItemRecipies(APIView):
    def get(self, request):
        itemRecipies = ItemRecipe.objects.all()
        serializer = serializers.ItemRecipiesSerializer(
            itemRecipies,
            many=True,
        )
        return Response(serializer.data)
