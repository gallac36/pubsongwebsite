from django.shortcuts import render
from .models import Song
from django.http import HttpResponse

# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songbook/song_list.html', {'songbook':songs})


def song_detail(request, slug):
#   return HttpResponse(slug)
    ASong = Song.objects.get(slug=slug)
    return render(request, 'songbook/song_detail.html', {'songbook':ASong})
