from rest_framework.serializers import ModelSerializer, SerializerMethodField
from champions.serializers import ChampionSerializer
from .models import Origin, Job


class OriginSerializer(ModelSerializer):
    champions = SerializerMethodField()

    class Meta:
        model = Origin
        fields = (
            "name",
            "description",
            "champions",
        )
        depth = 1

    def get_champions(self, obj):
        return ChampionSerializer(obj.champions.all(), many=True).data


class JobSerializer(ModelSerializer):
    champions = SerializerMethodField()

    class Meta:
        model = Job
        fields = (
            "name",
            "description",
            "champions",
        )
        depth = 1

    def get_champions(self, obj):
        return ChampionSerializer(obj.champions.all(), many=True).data
