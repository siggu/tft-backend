from rest_framework.serializers import ModelSerializer
from .models import Set11Augment, Set12Augment


class Set11AugmentSerializer(ModelSerializer):
    class Meta:
        model = Set11Augment
        fields = "__all__"

class Set12AugmentSerializer(ModelSerializer):
    class Meta:
        model = Set12Augment
        fields = "__all__"