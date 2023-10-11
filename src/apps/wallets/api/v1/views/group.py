from rest_framework import viewsets

from apps.wallets.models import WalletGroup
from apps.wallets.api.v1.serializers import group as serializers


class WalletGroupViewSet(viewsets.ModelViewSet[WalletGroup]):
    queryset = WalletGroup.objects.all()
    serializer_class = serializers.WalletGroupSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
