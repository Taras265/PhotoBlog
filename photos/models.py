from django.core.validators import FileExtensionValidator
from django.db import models


class AlbumType(models.Model):
    album_type = models.CharField(max_length=50, verbose_name='Тип альбому')

    def __str__(self):
        return self.album_type


class Album(models.Model):
    album = models.CharField(max_length=50, verbose_name='Альбом')
    description = models.TextField(max_length=150, verbose_name='Описаніє')
    album_type = models.ForeignKey(AlbumType, on_delete=models.CASCADE, verbose_name="Тип")

    def __str__(self):
        return self.album


class Photo(models.Model):
    photo = models.ImageField(verbose_name='Зображення')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом', blank=True, null=True)

    def __str__(self):
        return self.photo.name + " - " + str(self.album)


class Movie(models.Model):
    movie = models.FileField(verbose_name='Відіо', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом', blank=True, null=True)

    def __str__(self):
        return self.movie.name + " - " + str(self.album)
