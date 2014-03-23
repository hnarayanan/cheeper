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
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
