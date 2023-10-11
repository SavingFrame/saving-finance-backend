from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from mixins.models import DateTimeMixin, AuthorMixin


class Transaction(DateTimeMixin, AuthorMixin):  # type: ignore[django-manager-missing, explicit-override]
    amount = MoneyField(default=0.0, default_currency='USD', max_digits=10, decimal_places=2)
    category = models.ForeignKey('transactions.TransactionCategory', on_delete=models.PROTECT)
    wallet = models.ForeignKey('wallets.Wallet', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, default='')

