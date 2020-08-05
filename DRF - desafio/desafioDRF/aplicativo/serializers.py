from rest_framework import serializers
from aplicativo.models import Afazeres

class AfazeresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afazeres
        fields = '__all__'
        