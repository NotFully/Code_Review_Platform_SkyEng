from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_reviewer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomManager()
