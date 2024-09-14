from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Set11Augment, Set12Augment


# Create your views here.
class Set11Augments(APIView):
    def get(self, request):
        augments = Set11Augment.objects.all()
        serializer = serializers.Set11AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        augment_data_list = request.data
        response_data = []

        for augment_data in augment_data_list:
            augment_data_copy = augment_data.copy()
            serializer = serializers.Set11AugmentSerializer(data=augment_data_copy)

            if serializer.is_valid():
                augment_obj = serializer.save()
                augment_obj_serializer = serializers.Set11AugmentSerializer(augment_obj)
                response_data.append(augment_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error augment data:", augment_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)

class Set12Augments(APIView):
    def get(self, request):
        # isHidden이 False인 augment만 필터링
        augments = Set12Augment.objects.filter(isHidden=False)
        serializer = serializers.Set12AugmentSerializer(
            augments,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        augment_data_dict = request.data.get('augments', [])  # traits를 가져옴
        response_data = []

        for augment_data in augment_data_dict:
            augment_data_copy = augment_data.copy()

            # 이미지 URL 앞에 'https:' 붙이기
            if augment_data_copy.get('imageUrl', '').startswith('//'):
                augment_data_copy['imageUrl'] = 'https:' + augment_data_copy['imageUrl']
            
            # legendCodes 필드 처리
            if 'legendCodes' in augment_data_copy:
                for i, legendCode in enumerate(augment_data_copy['legendCodes']):
                    augment_data_copy[f'legendCode{i+1}'] = legendCode.get('legnedCode')
            
            serializer = serializers.Set12AugmentSerializer(data=augment_data_copy)

            if serializer.is_valid():
                augment_obj = serializer.save()
                augment_obj_serializer = serializers.Set12AugmentSerializer(augment_obj)
                response_data.append(augment_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error augment data:", augment_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)