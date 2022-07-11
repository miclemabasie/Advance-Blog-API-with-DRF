from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "pkid",
        "user",
        "phone",
        "gender",
        "proffessional",
        "country",
        "city",
    ]
    list_filter = ["country", "city"]


admin.site.register(Profile, ProfileAdmin)
