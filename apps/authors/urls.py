from django.urls import path
from .views import AuthorListAPIView


app_name = "authors"


urlpatterns = [
    path("", AuthorListAPIView.as_view(), name="authorlist-view"),
]
