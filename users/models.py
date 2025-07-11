from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'User'),
        (2, 'Admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    def is_admin(self):
        return self.role == 2

# Create your models here.
