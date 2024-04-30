from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import Champion

# Create your views here.


class Champions(APIView):
    def get(self, request):
        champions = Champion.objects.all()
        serializer = serializers.ChampionDetailSerializer(
            champions,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        champion_data_list = request.data  # 챔피언 데이터 리스트를 받습니다.
        response_data = []

        for champion_data in champion_data_list:
            champion_data_copy = (
                champion_data.copy()
            )  # 원본 데이터를 변경하지 않도록 복사합니다.

            # 반복되는 필드들을 정의합니다.
            repeated_fields = {
                "cost": 3,
                "health": 3,
                "attackDamage": 3,
                "damagePerSecond": 3,
            }

            # traits와 recommendItems 필드의 갯수를 확인하고 반복 횟수를 결정합니다.
            traits_count = len(champion_data_copy.get("traits", []))
            recommendItems_count = len(champion_data_copy.get("recommendItems", []))

            # traits와 recommendItems의 갯수를 확인하여 최대값을 사용합니다.
            max_traits = max(traits_count, 4)
            max_recommendItems = max(recommendItems_count, 5)

            # traits와 recommendItems의 갯수를 사용하여 반복 필드를 추가합니다.
            repeated_fields.update(
                {
                    "traits": max_traits,
                    "recommendItems": max_recommendItems,
                }
            )

            # 반복되는 필드들을 serializer 데이터에 추가합니다.
            for field, num in repeated_fields.items():
                for i in range(1, num + 1):
                    champion_data_copy[f"{field}{i}"] = (
                        champion_data_copy.get(field)[i - 1]
                        if i <= len(champion_data_copy.get(field, []))
                        else None
                    )

            # skill 객체를 수정합니다.
            skill_data = champion_data_copy.pop("skill", {})
            if skill_data:
                champion_data_copy.update(
                    {
                        "skill_name": skill_data.get("name"),
                        "skill_imageUrl": skill_data.get("imageUrl"),
                        "skill_desc": skill_data.get("desc"),
                        "skill_startingMana": skill_data.get("startingMana"),
                        "skill_skillMana": skill_data.get("skillMana"),
                    }
                )

                # skill_stats를 추가합니다.
                for i, stat in enumerate(skill_data.get("stats", []), start=1):
                    champion_data_copy[f"skill_stats{i}"] = stat

            # serializer를 초기화합니다.
            serializer = serializers.ChampionDetailSerializer(data=champion_data_copy)

            if serializer.is_valid():
                champion_obj = serializer.save()
                champion_obj_serializer = serializers.ChampionDetailSerializer(
                    champion_obj
                )
                response_data.append(champion_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error champion name :", champion_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)


class ChampionDetail(APIView):
    def get_object(self, key):
        try:
            return Champion.objects.get(key=key)
        except Champion.DoesNotExist:
            raise NotFound

    def get(self, reqeust, key):
        champion = self.get_object(key)
        serializer = serializers.ChampionDetailSerializer(
            champion,
        )
        return Response(serializer.data)
