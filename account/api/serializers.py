
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import authentication
from rest_framework import serializers
from account.models import Profile



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=["id","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined","groups","user_permissions"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields='__all__'
class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=['username','password']
        #password= make_password(['password'])

    def create(self, validated_data):
        user = User.objects.create(
            #email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
            )
        user.set_password(validated_data['password'])

        user.save()

        return user
