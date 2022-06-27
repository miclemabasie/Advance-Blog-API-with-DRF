from dataclasses import field
from django_countries import CountryTuple
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone = PhoneNumberField(source="profile.phone")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    full_name = serializers.SerializerMethodField(read_only=True)

    # profile_photo = serializers.

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "phone",
            "profile_photo",
            "city",
            "country",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        return obj.get_fullname

    def to_representation(self, instance):
        represention = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            represention["admin"] = True

        return represention


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
