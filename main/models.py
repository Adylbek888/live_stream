from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='media/main')
    hls_url = models.URLField(blank=True)
    is_encoding = models.BooleanField(default=False)