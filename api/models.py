"""  Models for the api of recordly. """
from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    """ Model for artists. """
    name = models.CharField(max_length=150, null=False, blank=False)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)


class Song(models.Model):
    """ Model for songs. """
    title = models.CharField(max_length=150, null=False, blank=False)
    length = models.FloatField(null=True, blank=False)
    artist_id = models.IntegerField(null=True)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)


class Album(models.Model):
    """ Model for albums. """
    title = models.CharField(max_length=200, null=False, blank=False)
    genre = models.CharField(max_length=100, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)
    released = models.DateField(null=True)
    artist = models.CharField(max_length=150, null=False, blank=False)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)
