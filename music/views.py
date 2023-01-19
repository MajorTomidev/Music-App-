from django.shortcuts import render
from .models import Album, Song
# Create your views here.

def album_page(request):
    all_albums = Album.objects.all()
    all_songs = Song.objects.all()
    
    context = {
        'all_albums': all_albums,
        'all_songs': all_songs
    }
    return render(request, 'music/home.html', context)