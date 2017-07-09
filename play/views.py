from django.shortcuts import render,reverse,redirect
from .models import Play
from car.models import Car
from django.http import Http404
from .forms import PlayForm,PartipateForm
from django.contrib import messages
# Create your views here.


def show_play_detail(request,slug):
    if not request.user.is_authenticated():
        return redirect('auth_login')
    play_obj = Play.objects.get(slug=slug)
    if request.user == play_obj.owner:
        return redirect('auth_logout')
    if request.method == "POST":
        play_obj.participants.add(request.user)
        play_obj.num_of_participants += 1
        play_obj.save()
        messages.success(request,'成功入局！')
        return redirect(reverse('play:play',kwargs={'slug':slug}))
    form = PartipateForm()
    context = {
        'play':play_obj,
        'form':form,
    }
    return render(request,'play/show_play_detail.html',context)

def create_play(request):
    if not request.user.is_authenticated():
        return redirect('auth_login')
    car_obj = Car.objects.get(slug='httpwwwbmwcom')
    if car_obj.play_object is not None:
        redirect(reverse('play:play',kwargs={'slug':car_obj.play_object.slug}))
    if request.method == "POST":
        form = PlayForm(request.POST)
        if form.is_valid():
            play = form.save(commit=False)
            play.owner = request.user
            play.save()
            car_obj = Car.objects.all()[0]
            car_obj.play_object = play
            car_obj.save()
            messages.success(request, 'Create Successfully')
            return redirect(reverse('play:play',kwargs={'slug':play.slug}))
        else:
            messages.error(request, 'Fail to Create')
    else:
        form = PlayForm()
    context = {
        "form": form,
    }
    return render(request, "play/play_form.html", context)

