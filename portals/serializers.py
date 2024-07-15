from rest_framework.serializers import ModelSerializer
from .models import Set11Portal, Set12Portal


class Set11PortalSerializer(ModelSerializer):
    class Meta:
        model = Set11Portal
        fields = "__all__"

class Set12PortalSerializer(ModelSerializer):
    class Meta:
        model = Set12Portal
        fields = "__all__"
