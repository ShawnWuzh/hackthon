from django.shortcuts import render,reverse,redirect
from .models import Car
# Create your views here.

def show_car_state(request,slug):
    car_obj = Car.objects.get(slug=slug)
    if car_obj.play_object is not None:
        play_obj = car_obj.play_object
        return redirect(reverse('play:play',kwargs={'slug':play_obj.slug}))
    else:
        return redirect(reverse('play:create_play'),car_url=car_obj.url)

