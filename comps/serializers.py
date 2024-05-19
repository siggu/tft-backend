# serializers.py
from rest_framework import serializers
from .models import Comp, CompElement


class CompElementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompElement
        fields = "__all__"


class CompElementReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompElement
        fields = "__all__"


class CompWriteSerializer(serializers.ModelSerializer):
    elements = CompElementWriteSerializer(many=True)

    class Meta:
        model = Comp
        fields = "__all__"

    def create(self, validated_data):
        elements_data = validated_data.pop("elements")
        comp = Comp.objects.create(**validated_data)
        for element_data in elements_data:
            CompElement.objects.create(comp=comp, **element_data)
        return comp


class CompReadSerializer(serializers.ModelSerializer):
    elements = CompElementReadSerializer(many=True)

    class Meta:
        model = Comp
        fields = "__all__"
