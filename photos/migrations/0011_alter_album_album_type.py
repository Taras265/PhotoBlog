# Generated by Django 3.2.7 on 2021-09-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20210915_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.albumtype', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
