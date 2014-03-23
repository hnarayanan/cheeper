from django.db import models

from custom_user.models import AbstractEmailUser
from model_utils.models import TimeStampedModel


class User(AbstractEmailUser):
    """
    A simple model to hold our users.
    """

    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=25, unique=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, default='')
    is_following = models.ManyToManyField('self', related_name='has_followers',
                                          symmetrical=False, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.name


# class FollowRelationship(TimeStampedModel):
#     """
#     A model to hold follower-followed relationships.
#     """

#     followed = models.ForeignKey(User, related_name='followed_user')
#     follower = models.ForeignKey(User, related_name='follower_user')

#     def __unicode__(self):
#         return '%s follows %s' % (self.follower, self.followed)
