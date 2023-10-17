from django.db import models
from djmoney.models.fields import MoneyField

from apps.wallets.utils import get_currency_symbol
from apps.wallets.models.group import WalletGroup
from mixins.models import DateTimeMixin, AuthorMixin
from saving_finance.middlewares import get_current_authenticated_user


def default_group():
    author = get_current_authenticated_user()
    if author is None:
        return None
    return WalletGroup.objects.get_or_create(author=author, name='Cash')[0]


class Wallet(DateTimeMixin, AuthorMixin):  # type: ignore
    name = models.CharField(max_length=128)
    balance = MoneyField(default=0.0, default_currency='USD', max_digits=14, decimal_places=2)
    group = models.ForeignKey('wallets.WalletGroup', on_delete=models.CASCADE, default=default_group)
    color = models.CharField(max_length=9, default='#ffa000')
    icon = models.CharField(max_length=50, default='radio-button-off-outline')

    @property
    def currency_symbol(self) -> str:
        return get_currency_symbol(self.balance.currency.code)
