from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class VerificationSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    otp = serializers.CharField()


class ForgotPasswordSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()


class ResetPasswordSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    otp = serializers.CharField()
