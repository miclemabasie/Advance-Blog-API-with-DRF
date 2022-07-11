from django.urls import path
from .views import (
    AuthorListAPIView,
    author_list_view,
    AuthorDetailAPIView,
    AuthorUpdateAPIView,
    AuthorDeleteAPIView,
)


app_name = "authors"


urlpatterns = [
    path("fun/", author_list_view),
    path("", AuthorListAPIView.as_view(), name="authorlist-view"),
    path("<int:pkid>/author/", AuthorDetailAPIView.as_view(), name="autho-detail"),
    path(
        "<int:pkid>/author/update/", AuthorUpdateAPIView.as_view(), name="update-author"
    ),
    path(
        "<int:pkid>/author/delete/", AuthorDeleteAPIView.as_view(), name="delete-author"
    ),
]
