from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'User'),
        (2, 'Admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    def is_admin(self):
        return self.role == 2

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
