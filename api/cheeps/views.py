from rest_framework import viewsets

from .models import Cheep
from .serializers import CheepSerializer


class CheepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cheeps to be viewed or edited.
    """
    queryset = Cheep.objects.all()
    serializer_class = CheepSerializer
