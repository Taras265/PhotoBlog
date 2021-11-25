from django.shortcuts import render, redirect
from photos.models import Album, Photo, Movie, AlbumType


def home(request):
    types = AlbumType.objects.all()
    return render(request, 'home.html', {'types': types})


def type_albums(request, t):
    if t:
        if len(Album.objects.filter(album_type=t)) == 1:
            return redirect('/album/'+str(Album.objects.filter(album_type=t)[0].pk))
        return render(request, 'type_albums.html', {'albums': Album.objects.filter(album_type=t)})


def album(request, pk):
    if pk:
        photos = Photo.objects.filter(album=pk)
        movies = Movie.objects.filter(album=pk)
        return render(request, 'album.html', {'photos': photos, 'movies': movies, 'album': Album.objects.get(pk=pk)})


def about(request):
    return render(request, 'about.html')
