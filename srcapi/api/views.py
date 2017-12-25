from django.shortcuts import render
from django.http import Http404
from .models import KeyWord,Value_Charater
from .serializers import KeyWordSerialize,ValueSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class KeyWord_Value(APIView):
        
    def get_value(self,key_word):
        try:
            return Value_Charater.objects.get(key_word=key_word)
            pass
        except Value_Charater.DoesNotExist:
            raise Http404
    def get(self, request, key_word, format=None):
        value = self.get_object(key_word)
        value = Value_Charater(value)
        return Response(value.data)

