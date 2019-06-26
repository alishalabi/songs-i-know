from django.shortcuts import render
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
    return HttpResponse("You're looking at song %s." % song_id)
