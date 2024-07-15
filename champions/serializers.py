from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Set11Champion, Set12Champion


class Set11ChampionSerializer(ModelSerializer):
    class Meta:
        model = Set11Champion
        fields = ("pk", "key", "name")
        depth = 1

class Set12ChampionSerializer(ModelSerializer):
    class Meta:
        model = Set12Champion
        fields = ("pk", "key", "name")
        depth = 1

class Set11ChampionDetailSerializer(ModelSerializer):
    class Meta:
        model = Set11Champion
        fields = "__all__"
        depth = 1

class Set12ChampionDetailSerializer(ModelSerializer):
    class Meta:
        model = Set12Champion
        fields = "__all__"
        depth = 1