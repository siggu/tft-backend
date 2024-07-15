from rest_framework import serializers
from .models import (
    Set11Comp, Set11CompElement, Set11ItemUsage, Set11MetaDeck,
    Set12Comp, Set12CompElement, Set12ItemUsage, Set12MetaDeck
)
from medias.serializers import PhotoSerializer
from champions.serializers import Set11ChampionDetailSerializer, Set12ChampionDetailSerializer

# Set 11 시리얼라이저들
class Set11CompElementSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    champion = Set11ChampionDetailSerializer(read_only=True)

    class Meta:
        model = Set11CompElement
        fields = "__all__"
        depth = 3

class Set11CompSerializer(serializers.ModelSerializer):
    elements = Set11CompElementSerializer(read_only=True, many=True)

    class Meta:
        model = Set11Comp
        fields = "__all__"
        depth = 2

class Set11MetaDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set11MetaDeck
        fields = "__all__"

class Set11ItemUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set11ItemUsage
        fields = "__all__"

# Set 12 시리얼라이저들
class Set12CompElementSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)
    champion = Set12ChampionDetailSerializer(read_only=True)

    class Meta:
        model = Set12CompElement
        fields = "__all__"
        depth = 3

class Set12CompSerializer(serializers.ModelSerializer):
    elements = Set12CompElementSerializer(read_only=True, many=True)

    class Meta:
        model = Set12Comp
        fields = "__all__"
        depth = 2

class Set12MetaDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set12MetaDeck
        fields = "__all__"

class Set12ItemUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set12ItemUsage
        fields = "__all__"
