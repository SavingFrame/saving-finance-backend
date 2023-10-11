from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from apps.core import models


class UserManager(BaseUserManager):

    def _create_user(
        self,
        email: str,
        password: str,
        is_staff: bool,
        is_superuser: bool,
        **extra_fields: dict
    ) -> 'models.User':
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user: 'core.User' = self.model(  # type: ignore
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user
