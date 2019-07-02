from django.urls import path
from .views import SongList, SongDetail

urlpatterns = [
    path("api/", SongList.as_view(), name="song_list"),
    path("api/<int:pk>/", SongDetail.as_view(), name="song_detail"),
]
