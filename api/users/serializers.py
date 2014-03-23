from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    thumbnail_url = serializers.CharField(source='thumbnail_url')

    class Meta:
        model = User
        cheeps = serializers.RelatedField(many=True)
        is_following = serializers.RelatedField(many=True)
        has_followers = serializers.RelatedField(many=True)
        fields = ('name', 'handle', 'thumbnail_url')
#        fields = ('url', 'name', 'handle', 'thumbnail', 'cheeps', 'is_following', 'has_followers')
