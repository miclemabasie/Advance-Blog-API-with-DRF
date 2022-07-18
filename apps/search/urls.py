from django.urls import path
from .views import ArticleSearchAPIView


urlpatterns = [
    path("article/", ArticleSearchAPIView.as_view(), name="article_search"),
    # path("profiles/")
]
