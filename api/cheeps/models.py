from django.db import models

from model_utils.models import TimeStampedModel


class Cheep(TimeStampedModel):
    """
    A simple model to hold our cheeps.
    """

    # author = models.ForeignKey(User, related_name="cheeps")
    content = models.CharField(max_length=140)
