from django.db import models

from mixins.models import DateTimeMixin, AuthorMixin


class WalletGroup(DateTimeMixin, AuthorMixin):
    name = models.CharField(max_length=128)
    