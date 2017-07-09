from django.conf.urls import url
from .views import show_play_detail,create_play
urlpatterns = [
    url(r'^create/$',create_play,name='create_play'),
    url(r'^(?P<slug>[\w-]+)/$',show_play_detail,name='play'),
]