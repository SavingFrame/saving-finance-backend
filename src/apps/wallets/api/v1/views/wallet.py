from rest_framework import viewsets

from apps.wallets.models import Wallet
from apps.wallets.api.v1.serializers import wallet as serializers


class WalletViewSet(viewsets.ModelViewSet[Wallet]):
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
