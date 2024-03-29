from rest_framework.serializers import ModelSerializer
from .models import Comp, CompElement
from medias.serializers import PhotoSerializer
from synergies.serializers import OriginSerializer, JobSerializer
from champions.serializers import ChampionDetailSerializer


class CompSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    origin = OriginSerializer(read_only=True, many=True)
    job = JobSerializer(read_only=True, many=True)
    champions = ChampionDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Comp
        fields = "__all__"
        depth = 3


class CompElementSerializer(ModelSerializer):
    class Meta:
        model = CompElement
        fields = "__all__"
