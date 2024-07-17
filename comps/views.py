from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from .models import Set11Comp, Set11CompElement, Set11ItemUsage, Set11MetaDeck, Set12Comp, Set12CompElement, Set12ItemUsage, Set12MetaDeck
from django.http import JsonResponse
from .meta_deck_generator import process_data_and_generate_meta_decks

class Set11Comps(APIView):
    def get(self, request):
        comps = Set11Comp.objects.all()
        serializer = serializers.Set11CompSerializer(
            comps,
            many=True,
        )
        return Response(serializer.data)

class Set11MetaDecks(APIView):
    def get(self, request):
        meta_decks = Set11MetaDeck.objects.all()
        serializer = serializers.Set11MetaDeckSerializer(meta_decks, many=True)
        return Response(serializer.data)
    def post(self, request):
        try:
            meta_decks, item_usage = process_data_and_generate_meta_decks()
            print("meta_decks",meta_decks)
            print("item_usage",item_usage)

            # 메타 덱 저장
            Set11MetaDeck.objects.all().delete()  # 기존 데이터 삭제
            for name, decks in meta_decks.items():
                print("name",name)
                print("decks",decks)
                serializer = serializers.Set11MetaDeckSerializer(data={'name': name, 'decks': decks})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # 아이템 사용량 저장
            Set11ItemUsage.objects.all().delete()  # 기존 데이터 삭제
            for champion, usages in item_usage.items():
                serializer = serializers.Set11ItemUsageSerializer(data={'name': champion, 'usages': usages})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": "success", "meta_decks": meta_decks, "item_usage": item_usage}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Set11MetaItems(APIView):
    def get(self, request):
        item_usage = Set11ItemUsage.objects.all()
        serializer = serializers.Set11ItemUsageSerializer(item_usage, many=True)
        return Response(serializer.data)


class Set12Comps(APIView):
    def get(self, request):
        comps = Set12Comp.objects.all()
        serializer = serializers.Set12CompSerializer(
            comps,
            many=True,
        )
        return Response(serializer.data)

class Set12MetaDecks(APIView):
    def get(self, request):
        meta_decks = Set12MetaDeck.objects.all()
        serializer = serializers.Set12MetaDeckSerializer(meta_decks, many=True)
        return Response(serializer.data)
    def post(self, request):
        try:
            meta_decks, item_usage = process_data_and_generate_meta_decks()

            # 메타 덱 저장
            Set12MetaDeck.objects.all().delete()  # 기존 데이터 삭제
            for name, decks in meta_decks.items():
                serializer = serializers.Set12MetaDeckSerializer(data={'name': name, 'decks': decks})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # 아이템 사용량 저장
            Set12ItemUsage.objects.all().delete()  # 기존 데이터 삭제
            for champion, usages in item_usage.items():
                serializer = serializers.Set12ItemUsageSerializer(data={'name': champion, 'usages': usages})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": "success", "meta_decks": meta_decks, "item_usage": item_usage}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Set12MetaItems(APIView):
    def get(self, request):
        item_usage = Set12ItemUsage.objects.all()
        serializer = serializers.Set12ItemUsageSerializer(item_usage, many=True)
        return Response(serializer.data)