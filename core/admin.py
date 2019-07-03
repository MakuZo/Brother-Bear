from django.contrib import admin

from core.models import ShortenedURL

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    fields = ('id', 'url')
    list_display = ('id', 'url')

