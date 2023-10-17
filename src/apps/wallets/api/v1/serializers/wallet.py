from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from apps.wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer[Wallet]):
    balance = MoneyField(max_digits=14, decimal_places=2, default=0.0)
    currency_symbol = serializers.CharField(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'
