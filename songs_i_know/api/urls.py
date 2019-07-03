from django.conf.urls import url
from django.urls import path, include
from .views import SongListViewSet  # , SongDetail
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'list', SongListViewSet, basename='songs')
# router.register(r'detail', SongDetail)


urlpatterns = [
    url(r'', include(router.urls)),
]
