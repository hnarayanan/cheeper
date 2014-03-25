import datetime
import jwt

from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    thumbnail_url = serializers.CharField(source='thumbnail_url', read_only=True)
    cheeps = serializers.HyperlinkedIdentityField(view_name='user-cheeps')
    following = serializers.HyperlinkedIdentityField(view_name='user-following')
    followers = serializers.HyperlinkedIdentityField(view_name='user-followers')

    class Meta:
        model = User
        fields = ('url', 'name', 'handle', 'thumbnail', 'thumbnail_url',
                  'cheeps', 'following', 'followers')
        write_only_fields = ('thumbnail',)

    # TOOD: Fix the following routine to create new users.
    # def restore_object(self, attrs, instance=None):
    #     """
    #     Instantiate a new User object.
    #     """
    #     user = User(email=attrs['email'], name=attrs['name'], handle=attrs['handle'])
    #     user.set_password(attrs['password'])
    #     return user


def jwt_payload_handler(user):
    return {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }


def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        api_settings.JWT_SECRET_KEY,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')


class AuthSerializer(serializers.Serializer):
    """
    Serializer class used to validate an email and password.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password"'
            raise serializers.ValidationError(msg)
