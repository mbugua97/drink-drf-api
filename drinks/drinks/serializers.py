from rest_framework.serializers import ModelSerializer
from . models import Drinks

class Drink_Serializer(ModelSerializer):
    class Meta:
        model=Drinks
        fields='__all__'

