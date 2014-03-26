from rest_framework import serializers

from users.serializers import CheepUserSerializer
from .models import Cheep


class CheepSerializer(serializers.HyperlinkedModelSerializer):

    author = CheepUserSerializer(read_only=True)

    class Meta:
        model = Cheep
        fields = ('url', 'created', 'modified', 'author', 'content')
