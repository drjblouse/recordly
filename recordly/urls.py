""" Url routes for api. """
from django.conf.urls import url, include, patterns
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewset)
router.register(r'albums', views.AlbumViewset)
router.register(r'songs', views.SongViewset)
router.register(r'users', views.UserViewSet)

slashless_router = routers.DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(slashless_router.urls)),
    url(r'^login', views.LoginView.as_view()),
]
