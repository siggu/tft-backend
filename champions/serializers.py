from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Champion, Skill
from medias.serializers import PhotoSerializer


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


class ChampionDetailSerializer(ModelSerializer):
    dps = SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Champion
        fields = "__all__"
        depth = 1

    def get_dps(self, obj):
        return obj.dps


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
