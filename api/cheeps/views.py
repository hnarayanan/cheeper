from rest_framework import viewsets
from rest_framework import permissions

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
