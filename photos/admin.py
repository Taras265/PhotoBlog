from django.contrib import admin
from photos.models import Photo, Album, Movie, AlbumType

admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Movie)
admin.site.register(AlbumType)
