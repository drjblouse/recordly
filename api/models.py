"""  Models for the api of recordly. """
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """ Base Model for keeping tables consistent. """
    last_updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(null=False)
    favorite = models.BooleanField()
    user = models.ForeignKey(User)


class Artist(BaseModel):
    """ Model for artists. """
    name = models.CharField(max_length=150, null=False, blank=False)


class Song(BaseModel):
    """ Model for songs. """
    title = models.CharField(max_length=150, null=False, blank=False)
    length = models.FloatField(null=False, blank=False)
    artist = models.ForeignKey(Artist)


class Album(BaseModel):
    """ Model for albums. """
    title = models.CharField(max_length=200, null=False, blank=False)
    genre = models.CharField(max_length=100, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)
    released = models.DateField(null=True)
    artist = models.ForeignKey(Artist)
    songs = models.ManyToManyField(Song)
