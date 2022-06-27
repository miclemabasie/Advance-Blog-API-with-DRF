from typing import ValuesView
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomUserManager(BaseUserManager):

    # Validate the user email
    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must pass in a valid email address."))

    def check_user_parameter(
        self, username, first_name, last_name, email, is_superuser=None
    ):

        if not username:
            raise ValueError(_("Username must be provided."))

        if not first_name:
            raise ValueError(_("First Name must be provided"))

        if not last_name:
            raise ValueError(_("Last Name must be provided."))

        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            if is_superuser:
                raise ValueError("A Superuser must provide an email address.")
            else:
                raise ValueError(_("Base Account: An email address must be provided"))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):

        self.check_user_parameter(username, first_name, last_name, email)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super user must have 'is_staff=True'"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super user must be have 'is_superus=True'"))

        if not password:
            raise ValueError(_("Super user must have a password"))

        if email:
            email = self.normalize_email(email)
            self.validate_email(email)
        else:
            raise ValueError(_("Admin User must provide an email address"))

        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
