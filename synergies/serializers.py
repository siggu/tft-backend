from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Trait


class TraitSerializer(ModelSerializer):
    class Meta:
        model = Trait
        fields = "__all__"
        depth = 1
