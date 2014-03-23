# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cheeps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cheep',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id'),
            preserve_default=True,
        ),
    ]
