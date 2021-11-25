from random import choice
from django import template
from photos.models import Photo, Album

register = template.Library()


@register.simple_tag
def first_photo(album):
    print(choice(Photo.objects.filter(album=album)))
    return choice(Photo.objects.filter(album=album)).photo.url


@register.simple_tag
def albums(t):
    return choice(list(Album.objects.filter(album_type=t)))
