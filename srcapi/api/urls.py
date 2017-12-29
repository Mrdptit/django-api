from django.conf.urls import url
from django.urls import path,re_path
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import *

user_list = UserViewSet.as_view({
    'post': 'creat_user'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update_user_info',
    'patch': 'partial_update',
    'delete': 'destroy'
})
chat = ChatViewSet.as_view({
    'post': 'key_value_data'
})
chat_value = ChatViewSet.as_view({
    'get':'get_key_value_data'
})


urlpatterns = [
    url(r'^learn$', chat),
    re_path(r'^chat/(?P<key>\w{1,50})/$', chat_value),
    re_path(r'^user/signin$', user_list),
    re_path(r'^user/token-auth/$', views.obtain_auth_token),
    path('user/update',user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)