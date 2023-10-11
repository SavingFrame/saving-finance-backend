from django.db import models
from djmoney.models.fields import MoneyField

from mixins.models import DateTimeMixin, AuthorMixin


class Wallet(DateTimeMixin, AuthorMixin):  # type: ignore
    name = models.CharField(max_length=128)
    balance = MoneyField(default=0.0, default_currency='USD', max_digits=14, decimal_places=2)
