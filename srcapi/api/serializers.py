from rest_framework import serializers
from .models import KeyWord,Value_Charater, User

class KeyWordSerialize(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('__all__')
class ValueSerialize(serializers.ModelSerializer):
    class Meta:
        model = Value_Charater
        fields = ('__all__')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')