from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Song


def index(request):
    # Query all songs
    all_songs = Song.objects.all()
    # template = loader.get_template('songapp/index.html')
    context = {
        'all_songs': all_songs,
    }
    # output = ', '.join([s.song_name for s in all_songs])
    return render(request, 'songapp/index.html', context)


def detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'songapp/detail.html', {'song': song})
