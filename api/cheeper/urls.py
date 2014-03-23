from django.conf.urls import patterns, include, url

from rest_framework import routers

from users.views import UserViewSet
from cheeps.views import CheepViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cheeps', CheepViewSet)

urlpatterns = patterns('',
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
