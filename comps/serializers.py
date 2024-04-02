from rest_framework.serializers import ModelSerializer
from .models import Comp, CompElement
from medias.serializers import PhotoSerializer
from synergies.serializers import OriginSerializer, JobSerializer
from champions.serializers import ChampionDetailSerializer


class CompElementSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    champion = ChampionDetailSerializer(read_only=True)

    origin = OriginSerializer(read_only=True, many=True)
    job = JobSerializer(read_only=True, many=True)

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
