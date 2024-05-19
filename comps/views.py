# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comp
from .serializers import CompWriteSerializer, CompReadSerializer


class Comps(APIView):
    def get(self, request):
        comps = Comp.objects.all()
        serializer = CompReadSerializer(comps, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        if isinstance(data, list):
            response_data = []
            for comp_data in data:
                serializer = CompWriteSerializer(data=comp_data)
                if serializer.is_valid():
                    serializer.save()
                    response_data.append(serializer.data)
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            serializer = CompWriteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
