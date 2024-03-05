from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Champion, Skill


class ChampionSerializer(ModelSerializer):
    class Meta:
        model = Champion
        fields = (
            "pk",
            "name",
            "cost",
            "avatar",
        )


class ChampionDetailSerializer(ModelSerializer):
    dps = SerializerMethodField()

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
