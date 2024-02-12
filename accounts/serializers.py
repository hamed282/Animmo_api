from rest_framework import serializers
from .models import User, OtpCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class OtpCodeRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpCode
        fields = ['phone_number', 'code', 'first_name', 'last_name']


class OtpCodeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpCode
        fields = ['phone_number', 'code']
