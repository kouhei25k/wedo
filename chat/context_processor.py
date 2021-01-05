from .models import Room


def common(request):
    context = {
        'room_list': request.user.joining_room.all()
    }
    return context
