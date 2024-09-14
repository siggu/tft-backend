from rest_framework.serializers import ModelSerializer
from .models import Set12Charm

class Set12CharmSerializer(ModelSerializer):
    class Meta:
        model = Set12Charm
        fields = "__all__"