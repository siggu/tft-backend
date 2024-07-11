from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from .models import Comp,ItemUsage,MetaDeck
from django.http import JsonResponse
from .meta_deck_generator import process_data_and_generate_meta_decks

class Comps(APIView):
    def get(self, request):
        comps = Comp.objects.all()
        serializer = serializers.CompSerializer(
            comps,
            many=True,
        )
        return Response(serializer.data)

class MetaDecks(APIView):
    def get(self, request):
        meta_decks = MetaDeck.objects.all()
        serializer = serializers.MetaDeckSerializer(meta_decks, many=True)
        return Response(serializer.data)
    def post(self, request):
        try:
            meta_decks, item_usage = process_data_and_generate_meta_decks()

            # 메타 덱 저장
            MetaDeck.objects.all().delete()  # 기존 데이터 삭제
            for name, decks in meta_decks.items():
                serializer = serializers.MetaDeckSerializer(data={'name': name, 'decks': decks})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # 아이템 사용량 저장
            ItemUsage.objects.all().delete()  # 기존 데이터 삭제
            for champion, usages in item_usage.items():
                serializer = serializers.ItemUsageSerializer(data={'name': champion, 'usages': usages})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": "success", "meta_decks": meta_decks, "item_usage": item_usage}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MetaItems(APIView):
    def get(self, request):
        item_usage = ItemUsage.objects.all()
        serializer = serializers.ItemUsageSerializer(item_usage, many=True)
        return Response(serializer.data)