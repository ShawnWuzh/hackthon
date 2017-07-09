from django.conf.urls import url
from .views import show_car_state
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$',show_car_state,name='car_state'),
]