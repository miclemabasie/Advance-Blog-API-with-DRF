from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
<<<<<<< HEAD
        fields = ["email", "username", "first_name", "last_name"]
=======
        fields = ["email", "username", "firlst_name", "last_name"]
>>>>>>> 4a8063e74fc079c99f434f97b83d654fa4c4f65a
        error_class = "errors"


class CustomUserChangeForm(UserChangeForm):
    model = User
<<<<<<< HEAD
    fields = ["email", "username", "first_name", "last_name"]
=======
    fields = ["email", "username", "firlst_name", "last_name"]
>>>>>>> 4a8063e74fc079c99f434f97b83d654fa4c4f65a
    error_class = "errors"
