from django.shortcuts import render,redirect
from chat.models import *
from accounts.models import CustomUser,UserRelationship
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def index(request):
    room_list = request.user.joining_room.all()
    friend_list = UserRelationship.objects.filter((Q(relating_user = request.user) | Q(related_user = request.user)) & Q(status = 'friend'))

    # friend_list = UserRelationship.objects.filter(Q(related_user = request.user)& Q(status = 'friend'))
    #user_list-frind_list
    notfriend_user_list = CustomUser.objects.exclude(Q(id = request.user.id) | Q(related_user__status = 'friend' ))
    context = {'room_list':room_list,'user_list':notfriend_user_list,'friend_list':friend_list}

    return render(request, 'chat/index.html',context)

@login_required
def room(request, room_name):
    message_list = Message.objects.filter(room=room_name).values('user__username','content').order_by('create_at')
    menber_list =  CustomUser.objects.filter(joining_room=room_name)
    room = Room.objects.get(id=room_name)
    context =   {'room': room,'message_list':message_list,'menber_list':menber_list}
    return render(request, 'chat/room.html', context)

@login_required
def createroom(request):
    room = Room()
    room.create_user = request.user
    room.name = request.POST.get("room_name")
    room.save()
    request.user.joining_room.add(room)

    return redirect("chat:index")

@login_required
def add_friend(request):

    if request.method == 'POST':
        friend_request_user = request.POST['action']
        relationship = UserRelationship()
        relationship.relating_user = request.user
        related_user = CustomUser.objects.get(id=friend_request_user)
        relationship.related_user = related_user
        relationship.status = 'friend'
        relationship.save()

    return redirect("chat:index")
    
def room_edit(request,room_name):
    menber_list =  CustomUser.objects.filter(joining_room=room_name)
    return render(request, 'chat/room_edit.html',{'menber_list':menber_list})


@login_required
def add_menber(request,room_name):
    if request.method == 'POST':
        select_user =  request.POST['action']
        print(select_user)
        user = CustomUser.objects.get(username=select_user)
        user.joining_room.add(room_name)
    

    #friend_list-menber_list
    appendable_friend_list = UserRelationship.objects.filter(relating_user = request.user,status = 'friend').exclude(related_user__joining_room=room_name)

    
    return render(request, 'chat/add_menber.html',{'friend_list':appendable_friend_list})