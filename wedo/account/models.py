from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import ArrayField


class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        elif not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
   
    joining_room = models.ManyToManyField('chat.Room',blank=True, related_name='joining_room')
    