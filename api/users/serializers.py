from rest_framework import serializers

from .models import User


class CheepUserSerializer(serializers.HyperlinkedModelSerializer):

    thumbnail_url = serializers.CharField(source='thumbnail_url', read_only=True)
    cheeps = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('name', 'handle', 'thumbnail_url')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    cheeps = serializers.HyperlinkedRelatedField(many=True, view_name='cheep-detail', read_only=True)
    is_following = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    has_followers = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'name', 'handle', 'thumbnail', 'cheeps', 'is_following', 'has_followers')
