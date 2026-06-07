from django.contrib import admin

from .models import Game, Genre, Studio, Platform, Review, UserProfile


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
	list_display = ('name', 'country', 'founding_year')
	search_fields = ('name', 'country', 'description')

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Review)
admin.site.register(UserProfile)