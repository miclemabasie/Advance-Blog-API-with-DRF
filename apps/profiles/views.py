from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileListSerializer


class ProfileListView(ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()


@api_view(["GET"])
def profile_list_view(request):
    queryset = Profile.objects.all()

    serializer = ProfileListSerializer(queryset, many=True)
    print(serializer.data)

    return Response(serializer.data)
