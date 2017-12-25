from rest_framework import serializers
from .models import KeyWord,Value_Charater

class KeyWordSerialize(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('id', 'key_word')
class ValueSerialize(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('id', 'key_word_id','value_key')