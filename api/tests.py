""" Tests for the recordly api. """
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate, \
    APIRequestFactory
from api.views import SongViewset, AlbumViewset, ArtistViewset


VIEWSET_DICT = {'get': 'list', 'post': 'create', 'put': 'update'}


def create_test_user():
    """ Create user for testing. """
    user = User.objects.create_user(
        'john', 'john@doe.com', 'secret')
    user.last_name = 'Doe'
    user.save()
    return user


def get_token():
    """ Authenticate for the tests. """
    user = create_test_user()
    token = Token.objects.create(user=user)
    return user, token


class LoginTests(APITestCase):
    """ Test cases for login api. """
    def test_login(self):
        """ Test the login functionality. """
        create_test_user()
        response = self.client.post(
            '/login', {'username': 'john', 'password': 'secret'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])
        response = self.client.post(
            '/login', {'username': 'john', 'password': 'bad'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.post(
            '/login', {'username': 'doh', 'password': 'pwd'})
        self.assertEqual(response.status_code,
                         status.HTTP_417_EXPECTATION_FAILED)
        response = self.client.post('/login', {'Bad request': 1})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AlbumTests(APITestCase):
    """ Test cases for album apis. """
    def test_get_albums(self):
        """ Ensure we can read album list. """
        factory = APIRequestFactory()
        view = AlbumViewset.as_view(VIEWSET_DICT)
        user, token = get_token()
        request = factory.get('/albums')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArtistTests(APITestCase):
    """ Test cases for artist apis. """
    def test_get_artists(self):
        """ Ensure we can read artist list. """
        factory = APIRequestFactory()
        view = ArtistViewset.as_view(VIEWSET_DICT)
        user, token = get_token()
        request = factory.get('/artists')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SongsTests(APITestCase):
    """ Test cases for song apis. """
    def test_get_songs(self):
        """ Ensure we can read song list. """
        factory = APIRequestFactory()
        view = SongViewset.as_view(VIEWSET_DICT)
        user, token = get_token()
        request = factory.get('/songs')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
