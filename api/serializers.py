
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class NavItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    path = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
