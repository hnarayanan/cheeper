# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelationship',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name=u'created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False)),
                ('followed', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('follower', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='is_following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, through='users.FollowRelationship', blank=True),
            preserve_default=True,
        ),
    ]
