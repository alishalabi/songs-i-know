from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from songapp.models import Song
from .serializers import SongSerializer


class SongListViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# class SongDetailViewSet(viewsets.ModelViewSet):
#     queryset = get_object_or_404(Song, pk=pk)
#     serializer_class = SongSerializer
