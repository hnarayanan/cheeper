from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Cheep


class CheepSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Cheep
        fields = ('url', 'created', 'modified', 'author', 'content')
