from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='studio_logos/',
        default='defaults/default_logo.jpg'
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    studio = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE
    )

    platforms = models.ManyToManyField(Platform)

    description = models.TextField(
        default='No description available.'
    )

    thumbnail = models.ImageField(
        upload_to='game_thumbnails/',
        default='defaults/default_image.jpg'
    )

    def __str__(self):
        return self.title