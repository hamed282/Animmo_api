from rest_framework import serializers
from .models import User, OtpCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class OtpCodeRegisterSerializer(serializers.Serializer):
        phone_number = serializers.CharField(max_length=20)
        code = serializers.CharField(max_length=20)
        first_name = serializers.CharField(max_length=50)
        last_name = serializers.CharField(max_length=50)


class OtpCodeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpCode
        fields = ['phone_number', 'code']
