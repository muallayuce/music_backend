from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.URLField()
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"


class RadioStation(models.Model):
    name = models.CharField(max_length=255)
    stream_url = models.URLField()

    def __str__(self):
        return self.name
