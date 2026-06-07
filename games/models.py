from datetime import date, datetime

from django.conf import settings
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, default='')

    founding_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(datetime.now().year)],
        null=True,
        blank=True,
        help_text='Year the studio was founded (optional)'
    )

    wallpaper = models.ImageField(
        upload_to='studio_wallpapers/',
        default='defaults/default_wallpaper.svg',
        blank=True,
        null=True
    )

    logo = models.ImageField(
        upload_to='studio_logos/',
        default='defaults/default_logo.png',
        blank=False,
        null=False
    )

    @property
    def age(self):
        if not self.founding_year:
            return None
        return date.today().year - self.founding_year

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    studio = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    platforms = models.ManyToManyField(Platform, blank=True)

    description = models.TextField(
        default='No description available.',
        validators=[MaxLengthValidator(2000)],
        blank=True,
        null=False
    )

    thumbnail = models.ImageField(
        upload_to='game_thumbnails/',
        default='defaults/default_image.jpg',
        blank=False,
        null=False
    )

    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    note = models.TextField(validators=[MaxLengthValidator(2000)], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.value} for {self.game} by {self.author}"


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    display_name = models.CharField(max_length=100, blank=True)
    public_handle = models.CharField(max_length=100, unique=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(
        upload_to='profile_avatars/',
        default='defaults/default_avatar.svg',
        blank=True
    )

    def save(self, *args, **kwargs):
        self.public_handle = self.user.username
        if not self.display_name:
            self.display_name = self.user.get_full_name() or self.user.username
        if not self.avatar:
            self.avatar = 'defaults/default_avatar.svg'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.display_name} (@{self.public_handle})'