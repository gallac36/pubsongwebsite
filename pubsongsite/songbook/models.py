from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    lyrics = models.TextField()
    author = models.CharField(max_length=50)
    chords = models.TextField(blank=True)


def __str__(self):
    return self.field_title
