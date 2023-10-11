from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.managers.user import UserManager


class User(AbstractUser):  # type: ignore[django-manager-missing]
    email = models.EmailField(
        unique=True,
        error_messages={'unique': 'User with that email already exists.'},
        help_text='Email',
    )
    username = None  # type: ignore

    USERNAME_FIELD = 'email'
    objects = UserManager()  # type: ignore

    REQUIRED_FIELDS = []
