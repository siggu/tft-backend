from rest_framework import serializers
from .models import SummonerPuuid, SummonerMatchesByPuuid


class SummonerPuuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerPuuid
        fields = "__all__"


class SummonerMatchesByPuuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerMatchesByPuuid
        fields = "__all__"
