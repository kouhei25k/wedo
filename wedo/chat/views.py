from django.shortcuts import render,redirect
from chat.models import *

def index(request):
    room_list = Room.objects.all()
    return render(request, 'chat/index.html',{'room_list':room_list})

def room(request, room_name):
    message_list = Message.objects.filter(room=room_name).order_by('create_at')

    return render(request, 'chat/room.html', {'room_name': room_name,'message_list':message_list,})

def createroom(request):
    room = Room()
    room.create_user = request.user
    room.name = request.POST.get("room_name")
    room.save()
    return  redirect("index", )