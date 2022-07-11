import profile
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import AuthorSerializer
from apps.profiles.models import Profile


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Profile.objects.filter(is_author=True)
