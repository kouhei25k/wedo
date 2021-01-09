from .models import Room
from accounts.models import CustomUser, UserRelationship
from django.db.models import Q


def common(request):
    if request.user.is_anonymous:
        room_list = None
        friend_list = None
    else:
        room_list = request.user.joining_room.all()
        friend_list = UserRelationship.objects.filter(
            (Q(relating_user=request.user) | Q(related_user=request.user)) & Q(status='friend'))

    # if request.method == 'GET':
    #     searched_user = None
    #     q_word = request.GET.get('query')
    #     if q_word:
    #         try:
    #             searched_user = CustomUser.objects.get(username=q_word)
    #         except SomeModel.DoesNotExist:
    #             searched_user = None

    context = {
        'room_list': room_list,
        'friend_list': friend_list,
        # 'searched_user': searched_user,
    }
    return context
