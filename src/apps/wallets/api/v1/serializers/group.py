from rest_framework import serializers

from apps.wallets.models import WalletGroup


class WalletGroupSerializer(serializers.ModelSerializer[WalletGroup]):
    class Meta:
        model = WalletGroup
        fields = '__all__'
