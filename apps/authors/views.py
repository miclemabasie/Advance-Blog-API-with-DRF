import profile
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.decorators import api_view
from .serializers import AuthorSerializer
from apps.profiles.models import Profile


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Profile.objects.filter(is_author=True)


class AuthorDetailAPIView(RetrieveAPIView):

    queryset = Profile.objects.filter(is_author=True)
    lookup_field = "pkid"
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.filter(is_author=True)
    lookup_field = "pkid"
    serializer_class = AuthorSerializer


class AuthorDeleteAPIView(DestroyAPIView):
    queryset = Profile.objects.filter(is_author=True)
    lookup_field = "pkid"
    serializer_class = AuthorSerializer


@api_view(["GET"])
def author_list_view(request):

    queryset = Profile.objects.filter(is_author=True)
    serializer = AuthorSerializer(queryset, many=True)

    return Response(serializer.data)
