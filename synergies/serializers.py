from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Set11Trait, Set12Trait


class Set11TraitSerializer(ModelSerializer):
    class Meta:
        model = Set11Trait
        fields = "__all__"
        depth = 1

class Set12TraitSerializer(ModelSerializer):
    class Meta:
        model = Set12Trait
        fields = "__all__"
        depth = 1
