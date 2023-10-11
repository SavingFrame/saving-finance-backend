from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from apps.wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer[Wallet]):
    balance = MoneyField()

    class Meta:
        model = Wallet
        fields = '__all__'
