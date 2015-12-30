""" Views for the recordly api. """
# Disabling non-relevant pylint issues due to django
# pylint: disable=too-many-ancestors
# pylint: disable=E1101
import logging
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Artist, Album, Song
from api.serializers import ArtistSerializer, \
    AlbumSerializer, SongSerializer


class ArtistViewset(viewsets.ModelViewSet):
    """ API endpoint for artists to be viewed and edited. """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewset(viewsets.ModelViewSet):
    """ API endpoint for albums to be viewed and edited. """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewset(viewsets.ModelViewSet):
    """ API endpoint for songs to be viewed and edited. """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


@permission_classes((AllowAny, ))
class LoginView(APIView):
    """ Login Post for getting auth token. """
    @staticmethod
    def post(request):
        """ POST request to obtain an auth token.
        :param request: The web request.
        """
        try:
            data = request.data
            if "username" not in data or "password" not in data:
                return Response('Invalid credentials',
                                status.HTTP_401_UNAUTHORIZED)
            user = User.objects.get(username=data['username'])
            password_valid = user.check_password(data['password'])
            if not user or not password_valid:
                logging.getLogger(__name__).debug('No user or bad password.')
                return Response('Invalid User.',
                                status.HTTP_404_NOT_FOUND)
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token[0].key})
        except (User.DoesNotExist, IndexError, KeyError, ParseError) as ex:
            logging.getLogger(__name__).error(ex)
            return Response('Invalid request.',
                            status.HTTP_417_EXPECTATION_FAILED)
