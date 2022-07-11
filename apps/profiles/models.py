from tabnanny import verbose
from turtle import numinput
import black
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.conf import settings
from apps.commons.models import TimeStampUUIDModel
from slugify import slugify


User = settings.AUTH_USER_MODEL


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(
        User, related_name="profile", verbose_name=_("User"), on_delete=models.CASCADE
    )
    about_me = models.TextField(verbose_name=_("Say something about yourself..."))
    phone = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+237670181442"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="profile_default.png"
    )

    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=100,
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    proffessional = models.CharField(
        verbose_name=_("What do you do for a living"), max_length=100
    )
    country = CountryField(
        verbose_name=_("Country"), max_length=100, default="CM", blank=True, null=True
    )
    city = models.CharField(
        verbose_name=_("City"), max_length=100, default="Bamenda", null=True, blank=True
    )
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    tiktok = models.CharField(max_length=255, blank=True, null=True)

    is_author = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
