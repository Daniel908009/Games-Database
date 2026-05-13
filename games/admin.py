from django.contrib import admin

from .models import Game, Genre, Studio, Platform

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Platform)