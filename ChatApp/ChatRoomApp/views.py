from .models import Room,Message
from django.shortcuts import render, redirect
from .forms import RoomForm
from django.utils.text import slugify

def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    members = messages.values_list('user__username', flat=True).distinct()
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages, 'members': members})

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.slug = slugify(room.name)
            room.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})

from django.http import HttpResponseBadRequest

def enter_room(request, slug):
    if request.method == 'POST':
        passkey = request.POST.get('passkey')
        room = Room.objects.get(slug=slug)
        if room.passkey == passkey:
            return redirect('room', slug=slug)
        else:
            return HttpResponseBadRequest("Incorrect passkey. Please try again.")
    else:
        return HttpResponseBadRequest("Invalid request method.")


