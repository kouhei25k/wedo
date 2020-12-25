from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser
# Create your models here.





class Room(models.Model):
    create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField("room_name", max_length=50)
    create_at=models.DateTimeField("create_at",default=timezone.now)
    class Meta:

        verbose_name_plural = "Room"

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    room = models.ForeignKey(Room,blank=True,null=True,related_name='message_room',on_delete=models.CASCADE)
    content = models.TextField()
    create_at=models.DateTimeField("create_at", default=timezone.now)
    class Meta:

        verbose_name_plural = "Message"

    def __str__(self):
        return self.content


class Todo(models.Model):
    create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    room = models.ForeignKey(Room,blank=True,null=True,related_name='todo_room',on_delete=models.CASCADE)
    what=models.CharField("what", max_length=50)
    how_much=models.PositiveSmallIntegerField("how_much")
    by_when=models.DateTimeField("by_when", auto_now=False, auto_now_add=False)
    punishment=models.CharField("punishment", max_length=50)
    create_at=models.DateTimeField("create_at", auto_now=True, auto_now_add=False)
    is_succeeded=models.BooleanField("is_succeeded",default=False)

    class Meta:
        verbose_name_plural = "Todo"

    def __str__(self):
        return self.what

