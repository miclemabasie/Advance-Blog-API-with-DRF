from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["pkid", "id", "username", "email", "first_name", "last_name"]
    list_filter = ["email", "is_staff", "is_active"]

    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": ("email", "password"),
            },
        ),
        (
            _("Personal Information"),
            {"fields": ("username", "first_name", "last_name")},
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("date_joined", "last_login")}),
    )

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2" "is_staff", "is_active"),
        },
    )

    search_fields = ("email", "username")


admin.site.register(User, UserAdmin)
