from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Champion, Skill
from medias.serializers import PhotoSerializer
from synergies.serializers import OriginSerializer, JobSerializer


class ChampionSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Champion
        fields = (
            "pk",
            "name",
            "cost",
            "photos",
        )
        depth = 1


class SkillSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Skill
        fields = "__all__"


class ChampionDetailSerializer(ModelSerializer):
    dps = SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)
    origin = OriginSerializer(read_only=True, many=True)
    job = JobSerializer(read_only=True, many=True)
    skill = SkillSerializer()

    class Meta:
        model = Champion
        fields = "__all__"
        depth = 1

    def get_dps(self, obj):
        return obj.dps
