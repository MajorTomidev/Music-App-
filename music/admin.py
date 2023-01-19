from django.contrib import admin
from .models import Album, Song 
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display =['title', 'artist']

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'album']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)