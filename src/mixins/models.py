from django.conf import settings
from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from saving_finance.middlewares import get_current_authenticated_user


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=get_current_authenticated_user,
        on_delete=models.CASCADE,
        blank=True,
    )

    class Meta(TypedModelMeta):
        abstract = True
        indexes = [
            HashIndex(fields=['author'], name='author_hash_idx')
        ]
