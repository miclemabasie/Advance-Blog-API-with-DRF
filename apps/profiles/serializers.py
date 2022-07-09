from rest_framework import serializers
from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username")
    short_name = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile

        fields = [
            "username",
            "about_me",
            "phone",
            "profile_photo",
            "gender",
            "proffessional",
            "country",
            "country",
            "city",
            "facebook",
            "twitter",
            "instagram",
            "tiktok",
            "short_name",
            "full_name",
        ]

    def get_short_name(self, obj):
        username = obj.user.username
        return username

    def get_full_name(self, obj):
        first_name = obj.user.first_name
        last_name = obj.user.last_name
        full_name = f"{first_name} {last_name}"
        return full_name
