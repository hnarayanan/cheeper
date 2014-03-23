from django.db import models

from model_utils.models import TimeStampedModel

from users.models import User


class Cheep(TimeStampedModel):
    """
    A simple model to hold our cheeps.
    """

    author = models.ForeignKey(User, related_name="cheeps")
    content = models.CharField(max_length=140)

    class Meta:
        ordering = ('-created',)
