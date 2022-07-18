from django.urls import path
from .views import (
    ArticleDeleteAPIView,
    ArticleListView,
    ArticleCreateAPIView,
    article_detail_api_view,
    UpdateArticleAPIView,
)

app_name = "articles"


urlpatterns = [
    path("create/", ArticleCreateAPIView.as_view(), name="article-create"),
    path("", ArticleListView.as_view(), name="article_list_view"),
    path("<int:pkid>/", article_detail_api_view, name="article_details"),
    path("<int:pkid>/update/", UpdateArticleAPIView.as_view(), name="update-article"),
    path("<int:pkid>/delete/", ArticleDeleteAPIView.as_view(), name="article_delete"),
]
