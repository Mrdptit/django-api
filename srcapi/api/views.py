from django.shortcuts import render
from django.http import Http404
from .models import KeyWord,Value_Charater,UserManager,User
from .serializers import KeyWordSerialize,ValueSerialize,UserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
import random
import json
import  logging
from django.views.decorators.csrf import csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def creat_user(self,request):
        print(request.data)
        logging.debug(request.data)
        email = request.data['email']
        password = request.data['password']
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        try:
            check_mail = User.objects.get(email = email)
            if check_mail:
                return Response({'status': status.HTTP_302_FOUND, 'msg': 'Email not exist'})
            pass
        except:
            user = User.objects.create_user(email = email, password = password)
            user.username = username
            user.first_name = first_name
            user.last_name  = last_name
            user.save()
            return Response({'status': status.HTTP_201_CREATED,'msg':'create success','data':UserSerializer(user).data})
    def update_user_info(self,request):
        try:
            id = request.PUT.get('id')
            print(id)
            user = User.objects.values_list().filter(id = id)
            print(user)
            username = request.PUT.get('username')
            first_name = request.PUT.get('first_name')
            last_name   = request.PUT.get('last_name')
            facebook_id = request.PUT.get('facebook_id')
            avatar = request.PUT.get('avatar')
            cover = request.PUT.get('cover')

            if user:
                if username:
                    user.username = username
                if cover:
                    user.cover = cover
                if first_name:
                    user.first_name = first_name
                if last_name:
                    user.last_name = last_name
                if facebook_id:
                    user.facebook_id = facebook_id
                if avatar:
                    user.avatar = avatar
                user.save()
                return Response({'status': status.HTTP_200_OK,'msg': 'udpate success'})
            pass
        except Exception as e:
            return Response({'status': status.HTTP_204_NO_CONTENT,'msg': 'no user'})

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Value_Charater.objects.all()
    serializer_class = ValueSerialize
    def get_value(key_word):
        try:
            return Value_Charater.objects.get(key_word=key_word)
            pass
        except Value_Charater.DoesNotExist:
            raise Http404
    @csrf_exempt
    def key_value_data(self,request,format= None):
        # value = ValueSerialize(data = request.POST.get)
        serializer = ValueSerialize(data=request.data)
        print(repr(serializer))
        print(serializer.is_valid())
        try:
            value = Value_Charater.objects.get(key_word=request.POST.get('key_word'),u_id=request.POST.get('u_id'),value_key=request.POST.get('value_key'))
            print(ValueSerialize(value).data)
        except Value_Charater.DoesNotExist:
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'sucess','status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        return Response({'msg':'Message has exist','status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    def get_key_value_data(self,request,key,format= None):
        message = request.GET.get('message')
        u_id = request.GET.get('id')
        print(u_id)
        print(message)
        print(key)
        try:
            value = Value_Charater.objects.all().filter(key_word=message)
            if u_id != None:
                value=value.filter(u_id = u_id)
            # print (value)
            if value:
                value = random.choice(value)
                value = ValueSerialize(value)
                print(value.data)
            return Response({'status': status.HTTP_200_OK, 'msg':'success','data': value.data['value_key']})
            pass
        except :
            return Response({'status': status.HTTP_204_NO_CONTENT,'msg':'no content', 'data': ''})
            raise e
        
        # def get(self, request, key_word, format=None):
        #     value = self.get_object(key_word)
        #     value = Value_Charater(value)
        #     return Response(value.data)
        # def post(self, request, format=None):
        #     serializer = ValueSerialize(data=request.DATA)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Create your views here.
