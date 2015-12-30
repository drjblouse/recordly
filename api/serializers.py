""" Serializers for recordly django rest api. """
from rest_framework import serializers
from api.models import Artist, Album, Song


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


class SongSerializer(serializers.ModelSerializer):
    """ Songs serializer. """
    class Meta(object):
        """ Meta class for serializer. """
        model = Song
