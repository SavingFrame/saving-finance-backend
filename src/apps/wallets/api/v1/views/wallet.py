from rest_framework import viewsets

from apps.wallets.models import Wallet
from apps.wallets.api.v1.serializers import wallet as serializers


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
