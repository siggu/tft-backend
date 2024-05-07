from rest_framework.serializers import ModelSerializer
from .models import Augment


class AugmentSerializer(ModelSerializer):
    class Meta:
        model = Augment
        fields = "__all__"
