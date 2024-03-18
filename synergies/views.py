from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


from . import serializers
from .models import Origin, Job, SynergyTier, SynergyStack


# Create your views here.
class Origins(APIView):
    def get(self, request):
        origins = Origin.objects.all()
        serializer = serializers.OriginSerializer(
            origins,
            many=True,
        )
        return Response(serializer.data)


class OriginName(APIView):
    def get_object(self, name):
        try:
            return Origin.objects.get(name=name)
        except Origin.DoesNotExist:
            raise NotFound

    def get(self, reqeust, name):
        origin = self.get_object(name)
        origin_data = []
        origin_info = {
            "id": origin.id,
            "name": origin.name,
            "synergy_champions": [
                {"champion_name": champion.name, "champion_pk": champion.pk}
                for champion in origin.champions.all()
            ],  # 여기서 champions Champion 모델에서 Origin에 대한 역참조 이름입니다.
        }
        origin_data.append(origin_info)

        serializer = serializers.OriginSerializer(origin_info)
        return Response(origin_info)


class Jobs(APIView):
    def get(self, reqeust):
        jobs = Job.objects.all()
        serializer = serializers.JobSerializer(
            jobs,
            many=True,
        )
        return Response(serializer.data)


class JobName(APIView):
    def get_object(self, name):
        try:
            return Job.objects.get(name=name)
        except Job.DoesNotExist:
            raise NotFound

    def get(self, reqeust, name):
        job = self.get_object(name)

        serializer = serializers.JobSerializer(job)
        return Response(serializer.data)


class SynergyTier(APIView):
    def get(self, request):
        synergyTiers = SynergyTier.objects.all()
        serializer = serializers.SynergyTierSerializer(
            synergyTiers,
            many=True,
        )
        return Response(serializer.data)


class SynergyStack(APIView):
    def get(self, request):
        synergyStacks = SynergyStack.objects.all()
        serializer = serializers.SynergyStackSerializer(
            synergyStacks,
            many=True,
        )
        return Response(serializer.data)
