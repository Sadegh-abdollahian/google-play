from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# from accounts.models import User
from applications.api.v1.serializers import AppSerializer
from accounts.models import OtpCode, BookMark
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=250)
    otp = serializers.CharField(max_length=4)

    class Meta:
        model = get_user_model()
        fields = ["phone_number", "username", "password", "password1", "otp"]

    def validate(self, attrs):
        phone = attrs.get("phone_number")
        otp = attrs.get("otp")
        code = OtpCode.objects.filter(phone_number=phone, code=otp).last()

        if not code:
            raise serializers.ValidationError({"Error": "Wrong otp code"})

        if attrs.get("password1") != attrs.get("password"):
            raise serializers.ValidationError({"Error": "Passwords mismatch"})

        try:
            validate_password(attrs.get("password"))
        except ValidationError as e:
            raise serializers.ValidationError({"Error": f"{e}"})

        return super().validate(attrs)

    def create(self, validate_data):
        validate_data.pop("password1")
        validate_data.pop("otp")
        validate_data["password"] = make_password(validate_data["password"])
        return super().create(validate_data)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    password1 = serializers.CharField(max_length=250)

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password1")

        user = authenticate(phone_number=phone_number, password=password)

        if user is not None:
            attrs["user"] = user
            return attrs
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class BookMarkSerializer(serializers.Serializer):
    user = PhoneNumberSerializer()
    app = AppSerializer()

    class Meta:
        model = BookMark
        fields = ["user", "app"]
