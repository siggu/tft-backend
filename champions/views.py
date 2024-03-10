from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import Champion, Skill

# Create your views here.


class Champions(APIView):
    def get(self, request):
        champions = Champion.objects.all()
        serializer = serializers.ChampionSerializer(
            champions,
            many=True,
        )
        return Response(serializer.data)


class ChampionDetail(APIView):
    def get_object(self, pk):
        try:
            return Champion.objects.get(pk=pk)
        except Champion.DoesNotExist:
            raise NotFound

    def get(self, reqeust, pk):
        champion = self.get_object(pk)
        serializer = serializers.ChampionDetailSerializer(
            champion,
        )
        return Response(serializer.data)


class Skills(APIView):
    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise NotFound

    def get(self, reqeust, pk):
        skill = self.get_object(pk)
        serializer = serializers.SkillSerializer(
            skill,
        )
        return Response(serializer.data)
