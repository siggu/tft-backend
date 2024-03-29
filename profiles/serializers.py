from rest_framework import serializers
from .models import SummonerPuuid


class SummonerPuuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummonerPuuid
        fields = "__all__"
