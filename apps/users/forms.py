from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "errors"


class CustomUserChangeForm(UserChangeForm):
    model = User
    fields = ["email", "username", "first_name", "last_name"]
    error_class = "errors"
