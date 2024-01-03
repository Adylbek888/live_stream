from django.contrib import admin
from . models import Video

@admin.register(Video)
class AdminVideo(admin.ModelAdmin):
    list_display = ['title','video_file','hls_url','is_encoding']

    class Meta():
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'