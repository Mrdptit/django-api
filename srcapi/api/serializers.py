from rest_framework import serializers
from .models import KeyWord,Value_Charater, User,random_generator
from django.contrib.auth import update_session_auth_hash
class KeyWordSerialize(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('__all__')
class ValueSerialize(serializers.ModelSerializer):
    class Meta:
        model = Value_Charater
        fields = ('__all__')
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('email','password','id','last_name','first_name','username','token',
        'facebook_id','avatar','cover','verifyUser','verify_key','active','confirm_password',
        )
        read_only_fields = ('create_date','active','staff','admin','is_superuser')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',
                                               instance.username)
        instance.first_name = validated_data.get('first_name',
                                                instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                               instance.last_name)
        instance.avatar = validated_data.get('avatar',
                                               instance.avatar)
        instance.avatar = validated_data.get('cover',
                                               instance.cover)
        instance.avatar = validated_data.get('facebook_id',
                                               instance.facebook_id)
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)
        instance.save()
        return instance

    def validate(self, data):
        '''
        Ensure the passwords are the same
        '''
        if data['password']:
            print ("Here")
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data