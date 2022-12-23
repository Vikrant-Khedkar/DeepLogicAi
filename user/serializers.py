from rest_framework import serializers
from django.contrib.auth.models import User
from . models import *


class textSerializer(serializers.ModelSerializer):
    class Meta:
        model = text
        fields = ('text','pdf','user')

# class getpdf(serializers.Serializer):
    # user = serializers.IntegerField()
    # pdf = serializers.URLField()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = pdf
        fields = ('pdf','user')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user