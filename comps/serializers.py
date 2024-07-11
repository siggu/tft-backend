from rest_framework.serializers import ModelSerializer
from .models import Comp, CompElement, ItemUsage, MetaDeck
from medias.serializers import PhotoSerializer
from champions.serializers import ChampionDetailSerializer


class CompElementSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    champion = ChampionDetailSerializer(read_only=True)

    class Meta:
        model = CompElement
        fields = "__all__"
        depth = 3


class CompSerializer(ModelSerializer):
    elements = CompElementSerializer(read_only=True, many=True)

    class Meta:
        model = Comp
        fields = "__all__"
        depth = 2

class MetaDeckSerializer(ModelSerializer):
    class Meta:
        model = MetaDeck
        fields="__all__"

class ItemUsageSerializer(ModelSerializer):
    class Meta:
        model = ItemUsage
        fields="__all__"