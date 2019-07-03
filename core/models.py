from django.db import models

class ShortenedURL(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True)
    url = models.URLField()