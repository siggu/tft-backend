from rest_framework.serializers import ModelSerializer
from .models import Portal


class PortalSerializer(ModelSerializer):
    class Meta:
        model = Portal
        fields = "__all__"
