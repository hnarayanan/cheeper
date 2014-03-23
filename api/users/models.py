from django.db import models

from custom_user.models import AbstractEmailUser
from model_utils.models import TimeStampedModel


class User(AbstractEmailUser):
    """
    A simple model to hold our users.
    """

    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=25)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    is_following = models.ManyToManyField('self', through='FollowRelationship' , symmetrical=False, related_name='has_followers', null=True, blank=True)


class FollowRelationship(TimeStampedModel):

    followed = models.ForeignKey(User, related_name='follower_user')
    follower = models.ForeignKey(User, related_name='followed_user')
