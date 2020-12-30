from .models import Room


def common(request):
    context = {
        'room_list': Room.objects.all()
    }
    return context
