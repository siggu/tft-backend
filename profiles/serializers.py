from rest_framework import serializers
from .models import (
    SummonerPuuid,
    SummonerMatchesByPuuid,
    SummonerMatchByMatchId,
    MatchDetailsByMatchId,
)


class SummonerPuuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerPuuid
        fields = "__all__"


class SummonerMatchesByPuuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerMatchesByPuuid
        fields = "__all__"


class SummonerMatchByMatchIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerMatchByMatchId
        fields = "__all__"


class MatchDetailsByMatchIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetailsByMatchId
        fields = "__all__"
