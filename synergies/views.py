from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import Set11Trait, Set12Trait


# Create your views here.
class Set11Traits(APIView):
    def get(self, request):
        traits = Set11Trait.objects.all()
        serializer = serializers.Set11TraitSerializer(
            traits,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        trait_data_list = request.data
        response_data = []

        for trait_data in trait_data_list:
            trait_data_copy = trait_data.copy()
            serializer = serializers.Set11TraitSerializer(data=trait_data_copy)

            if serializer.is_valid():
                trait_obj = serializer.save()
                trait_obj_serializer = serializers.Set11TraitSerializer(trait_obj)
                response_data.append(trait_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error trait data:", trait_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)


class Set12Traits(APIView):
    def get(self, request):
        # isHidden이 False인 trait만 필터링
        traits = Set12Trait.objects.filter(isHidden=False)
        serializer = serializers.Set12TraitSerializer(traits, many=True)
        return Response(serializer.data)

    def post(self, request):
        trait_data_dict = request.data.get('traits', [])  # traits를 가져옴
        response_data = []

        for trait_data in trait_data_dict:
            trait_data_copy = trait_data.copy()
            # "type" 필드를 "_type"으로 매핑
            trait_data_copy["_type"] = trait_data.pop("type", None)

            # 이미지 URL 앞에 'https:' 붙이기
            if trait_data_copy.get('imageUrl', '').startswith('//'):
                trait_data_copy['imageUrl'] = 'https:' + trait_data_copy['imageUrl']
            if trait_data_copy.get('blackImageUrl', '').startswith('//'):
                trait_data_copy['blackImageUrl'] = 'https:' + trait_data_copy['blackImageUrl']
            if trait_data_copy.get('whiteImageUrl', '').startswith('//'):
                trait_data_copy['whiteImageUrl'] = 'https:' + trait_data_copy['whiteImageUrl']
            
            # 스타일 필드 처리
            if 'styles' in trait_data_copy:
                for i, style in enumerate(trait_data_copy['styles']):
                    trait_data_copy[f'style{i+1}'] = style.get('style')
                    trait_data_copy[f'style{i+1}_min'] = style.get('min')
                    trait_data_copy[f'style{i+1}_max'] = style.get('max', None)
            
            # stats 필드 처리
            if 'stats' in trait_data_copy:
                stats = trait_data_copy['stats']
                for i, (key, value) in enumerate(sorted(stats.items()), start=1):
                    trait_data_copy[f'stats{i}'] = f"({key}) {value}"

            serializer = serializers.Set12TraitSerializer(data=trait_data_copy)

            if serializer.is_valid():
                trait_obj = serializer.save()
                trait_obj_serializer = serializers.Set12TraitSerializer(trait_obj)
                response_data.append(trait_obj_serializer.data)
            else:
                response_data.append(serializer.errors)

        return Response(response_data)

    def delete(self, requets):
        triats = Set12Traits.objects.all()
        triats.delete()
        return Response(status=status.HTTP_200_OK)