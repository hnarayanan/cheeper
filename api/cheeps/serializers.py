from rest_framework import serializers

from .models import Cheep


class CheepSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cheep
        fields = ('url', 'author', 'content', 'created')
