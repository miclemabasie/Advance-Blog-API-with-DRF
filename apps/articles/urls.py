from django.urls import path
from .views import ArticleListView, article_detail_api_view

app_name = "articles"


urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list_view"),
    path("<int:pkid>/", article_detail_api_view, name="article_details"),
]
