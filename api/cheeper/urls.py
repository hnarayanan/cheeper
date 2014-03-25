from django.conf import settings
from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import ObtainJSONWebToken

from users.serializers import AuthSerializer
from users.views import UserViewSet, UserFollowingViewSet, UserFollowerViewSet
from cheeps.views import CheepViewSet, UserCheepViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cheeps', CheepViewSet)

urlpatterns = patterns('',
  url(r'^', include(router.urls)),
  url(r'^users/(?P<pk>[0-9]+)/cheeps/$', UserCheepViewSet.as_view({'get': 'list'}), name='user-cheeps'),
  url(r'^users/(?P<pk>[0-9]+)/following/$', UserFollowingViewSet.as_view({'get': 'list'}), name='user-following'),
  url(r'^users/(?P<pk>[0-9]+)/followers/$', UserFollowerViewSet.as_view({'get': 'list'}), name='user-followers'),

  url(r'^auth-session/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^auth-token/', ObtainJSONWebToken.as_view(serializer_class=AuthSerializer)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
