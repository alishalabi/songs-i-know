from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Song


class IndexView(generic.ListView):
    # model = Song
    template_name = 'songapp/index.html'
    context_object_name = 'all_songs'
    # all_songs = Song.objects.all()
    # context = {
    #     'all_songs': all_songs,
    # }

    def get_queryset(self):
        return Song.objects.all()


class DetailView(generic.DetailView):
    model = Song
    # song = get_object_or_404(Song, pk=song_id)
    # return render(request, 'songapp/detail.html', {'song': song})
    template_name = "songapp/detail.html"
