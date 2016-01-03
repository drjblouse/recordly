""" Serializers for recordly django rest api. """
from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Artist, Album, Song


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ User serializer. """
    class Meta(object):
        """ Meta class for serializer. """
        model = User
        fields = ('id', 'username', 'email')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """ Artist serializer. """
    class Meta(object):
        """ Meta class for serializer. """
        model = Artist


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """ Album serializer. """
    class Meta(object):
        """ Meta class for serializer. """
        model = Album
        fields = ('id', 'url', 'title', 'genre',
                  'label', 'released', 'artist', 'favorite')


class SongSerializer(serializers.ModelSerializer):
    """ Songs serializer. """
    class Meta(object):
        """ Meta class for serializer. """
        model = Song
