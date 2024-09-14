from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Set11Item, Set12Item
from rest_framework import status


# Create your views here.
class Set11Items(APIView):
    def get(self, request):
        # isHidden이 False인 item만 필터링
        items = Set11Item.objects.filter(isHidden=False)
        serializer = serializers.Set11ItemSerializer(
            items,
            many=True,
        )
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = serializers.ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         item_obj = serializer.save()
    #         item_obj_serializer = serializers.ItemSerializer(item_obj)

    #         return Response(item_obj_serializer.data)
    #     else:
    #         print("serializer error!!!!")
    #         print(serializer.errors)
    #         return Response(serializer.errors)

    def post(self, request):
        item_data_dict = request.data.get('items', [])  # items를 가져옴
        response_data = []

        for item_data in item_data_dict:
            item_data_copy = item_data.copy()

            # 이미지 URL 앞에 'https:' 붙이기
            if item_data_copy.get('imageUrl', '').startswith('//'):
                item_data_copy['imageUrl'] = 'https:' + item_data_copy['imageUrl']

            # compositions 필드 처리
            if 'compositions' in item_data_copy:
                for i, composition in enumerate(item_data_copy['compositions']):
                    item_data_copy[f'composition{i+1}'] = composition

            serializer = serializers.Set11ItemSerializer(data=item_data_copy)

            if serializer.is_valid():
                item_obj = serializer.save()
                item_obj_serializer = serializers.Set11ItemSerializer(item_obj)
                response_data.append(item_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error item data:", item_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)


class Set12Items(APIView):
    def get(self, request):
        # isHidden이 False인 item만 필터링
        items = Set12Item.objects.filter(isHidden=False)
        serializer = serializers.Set12ItemSerializer(
            items,
            many=True,
        )
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = serializers.ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         item_obj = serializer.save()
    #         item_obj_serializer = serializers.ItemSerializer(item_obj)

    #         return Response(item_obj_serializer.data)
    #     else:
    #         print("serializer error!!!!")
    #         print(serializer.errors)
    #         return Response(serializer.errors)

    def post(self, request):
        item_data_dict = request.data.get('items', [])  # items를 가져옴
        response_data = []

        for item_data in item_data_dict:
            item_data_copy = item_data.copy()

            # 이미지 URL 앞에 'https:' 붙이기
            if item_data_copy.get('imageUrl', '').startswith('//'):
                item_data_copy['imageUrl'] = 'https:' + item_data_copy['imageUrl']

            # compositions 필드 처리
            if 'compositions' in item_data_copy:
                for i, composition in enumerate(item_data_copy['compositions']):
                    item_data_copy[f'composition{i+1}'] = composition

            serializer = serializers.Set12ItemSerializer(data=item_data_copy)

            if serializer.is_valid():
                item_obj = serializer.save()
                item_obj_serializer = serializers.Set12ItemSerializer(item_obj)
                response_data.append(item_obj_serializer.data)
            else:
                print("serializer error!!!!")
                print("error item data:", item_data_copy)
                print(serializer.errors)
                response_data.append(serializer.errors)

        return Response(response_data)
    
    def delete(self, requets):
        items = Set12Item.objects.all()
        items.delete()
        return Response(status=status.HTTP_200_OK)