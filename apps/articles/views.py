from os import set_inheritable
from tkinter.tix import STATUS
from unittest import installHandler
from django.http import Http404
from django.shortcuts import render
from requests import Response
from .models import Article
from .serializers import (
    ArticleSerializer,
    UpdateArticleSerializer,
    CreateArticleSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(["GET"])
def article_detail_api_view(request, pkid):
    # try:
    #     article = Article.objects.get(pkid=pkid)
    # except Article.DoesNotExist:
    #     raise Http404("Product with this credentials not found.")

    article = get_object_or_404(Article, pkid=pkid)
    print("$$$$$$$$$$$")
    print(article)

    serialiser = ArticleSerializer(Article).data

    return Response(article)


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pkid"


article_detail_api_view = ArticleDetailAPIView.as_view()


class UpdateArticleAPIView(UpdateAPIView):
    serializer_class = UpdateArticleSerializer
    queryset = Article.objects.filter(is_published=True)
    lookup_field = "pkid"


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = CreateArticleSerializer
    queryset = Article.objects.all()


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pkid"
