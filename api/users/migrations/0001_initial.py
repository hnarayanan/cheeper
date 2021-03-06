# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name=u'password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'last login')),
                ('is_superuser', models.BooleanField(default=False, help_text=u'Designates that this user has all permissions without explicitly assigning them.', verbose_name=u'superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=u'email address', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text=u'Designates whether the user can log into this admin site.', verbose_name=u'staff status')),
                ('is_active', models.BooleanField(default=True, help_text=u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name=u'active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'date joined')),
                ('name', models.CharField(max_length=200)),
                ('handle', models.CharField(max_length=25)),
                ('thumbnail', models.ImageField(default='', upload_to='thumbnails/', blank=True)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name=u'groups', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name=u'user permissions', blank=True)),
            ],
            options={
                u'abstract': False,
                u'verbose_name': u'user',
                u'verbose_name_plural': u'users',
            },
            bases=(models.Model,),
        ),
    ]
