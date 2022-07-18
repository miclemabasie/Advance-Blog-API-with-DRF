from tokenize import maybe
from django.shortcuts import render
from apps.articles.models import Article, Category
from apps.articles.serializers import ArticleSerializer
from apps.profiles.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleSearchAPIView(APIView):
    serializer_class = ArticleSerializer

    def post(self, request):
        queryset = Article.objects.filter(is_published=True)

        data = self.request.data

        print("333333333333333333333333", self.request.data["title"])

        serializer = ArticleSerializer(
            queryset, many=True, context={"request": self.request}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
