
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from model_utils.fields import StatusField
from model_utils import Choices


class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        elif not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    joining_room = models.ManyToManyField(
        'chat.Room', blank=True, related_name='joining_room')


class UserRelationship(models.Model):
    STATUS = Choices('friend', 'unrelated', 'blocked')
    relating_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_query_name='relating_user', null=True)
    related_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='related_user', null=True)
    status = StatusField(default='unrelated',)
