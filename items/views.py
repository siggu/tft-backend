from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Item


# Create your views here.
class Items(APIView):
    def get(self, request):
        augments = Item.objects.all()
        serializer = serializers.ItemSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)