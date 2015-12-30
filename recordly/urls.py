""" Url routes for api. """
from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewset)
router.register(r'albums', views.AlbumViewset)
router.register(r'songs', views.SongViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login', views.LoginView.as_view()),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework'))
]
