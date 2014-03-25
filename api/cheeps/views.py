from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from users.models import User
from .models import Cheep
from .serializers import CheepSerializer
from .permissions import IsAuthorOrReadOnly


class CheepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cheeps to be viewed or edited.
    """
    queryset = Cheep.objects.all()
    serializer_class = CheepSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class UserCheepViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves cheeps by a given author.
    """
    def list(self, request, pk=None):
       author = get_object_or_404(User, pk=pk)
       queryset = author.cheeps.all()
       serializer = CheepSerializer(queryset, many=True)
       return Response(serializer.data)
