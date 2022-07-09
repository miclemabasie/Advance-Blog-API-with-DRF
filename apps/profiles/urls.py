from .views import ProfileListView, profile_list_view
from django.urls import path

app_name = "profiles"

urlpatterns = [
    path("fun/", profile_list_view),
    path("", ProfileListView.as_view(), name="profile-list-view"),
]
