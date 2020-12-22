from django.db import models
from django.utils import timezone

# Create your models here.
# class Todo(models.Model):
#     create_user = ForeignKey(get_user_model(),on_delete=CASCADE)
#     what=models.CharField(_("what"), max_length=50)
#     how_much=models.PositiveSmallIntegerField(_("how_much"), )
#     by_when=models.models.DateTimeField(_("by_when"), auto_now=False, auto_now_add=False)
#     punishment=models.CharField(_("punishment"), max_length=50)
#     create_at=models.DateTimeField(_("create_at"), auto_now=True, auto_now_add=False)
#     is_succeeded=models.BooleanField(_("is_succeeded"),default=False)

#     class Meta:

#         verbose_name_plural = "Todo"

#     def __str__(self):
#         return self.what


class Room(models.Model):
    # create_user = ForeignKey(get_user_model(),on_delete=CASCADE)
    name = models.CharField("room_name", max_length=50)
    create_at=models.DateTimeField("create_at",default=timezone.now)
    class Meta:

        verbose_name_plural = "Room"

    def __str__(self):
        return self.name

class Message(models.Model):
    # user = ForeignKey(get_user_model(),on_delete=CASCADE)
    user = models.CharField('user',max_length=50)
    room = models.ForeignKey(Room,blank=True,null=True,related_name='room_meesages',on_delete=models.CASCADE)
    content = models.TextField()
    create_at=models.DateTimeField("create_at", default=timezone.now)
    class Meta:

        verbose_name_plural = "Message"

    def __str__(self):
        return self.content


