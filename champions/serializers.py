from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Champion


class ChampionSerializer(ModelSerializer):
    class Meta:
        model = Champion
        fields = (
            "pk",
            "key",
            "name",
        )
        depth = 1


class ChampionDetailSerializer(ModelSerializer):
    class Meta:
        model = Champion
        fields = "__all__"
        depth = 1
