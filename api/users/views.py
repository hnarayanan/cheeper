from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserFollowingViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves the list of users a given user is
    following.
    """
    def list(self, request, pk=None):
       author = get_object_or_404(User, pk=pk)
       queryset = author.is_following.all()
       serializer = UserSerializer(queryset, many=True)
       return Response(serializer.data)


class UserFollowerViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves the list of users a following a given
    user.
    """
    def list(self, request, pk=None):
       author = get_object_or_404(User, pk=pk)
       queryset = author.has_followers.all()
       serializer = UserSerializer(queryset, many=True)
       return Response(serializer.data)
