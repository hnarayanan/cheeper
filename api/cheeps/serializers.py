from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Cheep


class CheepSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Cheep
        fields = ('url', 'author', 'content', 'created')
