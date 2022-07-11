from rest_framework import serializers

# from phonenumber_field.serializerfields import PhoneNumberField
from django_countries.fields import CountryField
from apps.profiles.models import Profile


class AuthorSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source="user.username")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    # phone_number = PhoneNumberField()
    country = CountryField()

    articles = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            # "phone_number",
            "email",
            "profile_photo",
            "gender",
            "proffessional",
            "country",
            "city",
            "facebook",
            "twitter",
            "is_author",
            "articles",
        ]

    def get_articles(self, obj):
        if hasattr(obj, "articles"):
            return None
        else:
            return None
