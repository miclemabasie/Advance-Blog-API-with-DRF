from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
