from django.db import models

from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    """

    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=25)
    thumbnail = models.ImageField(upload_to='thumbnails/')
