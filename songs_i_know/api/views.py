from django.shortcuts import render

# Create your views here.
from rest_framwork.views import APIView
from rest_framework.response import Response
from djano.shortcuts import get_object_or_404

from .models import Song
from .serializers import SongSerializer


class SongList(APIView):
    def get(self, request):
        songs = Song.objects.all()
        data = SongSerializer(songs, many=True).data
        return Response(data)


class SongDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Song, pk=pk)
        data = SongSerializer(song).data
        return Response(data)
