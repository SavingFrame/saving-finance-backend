from rest_framework import viewsets

from apps.wallets.models import WalletGroup
from apps.wallets.api.v1.serializers import group as serializers


class WalletGroupViewSet(viewsets.ModelViewSet):
    queryset = WalletGroup.objects.all()
    serializer_class = serializers.WalletGroupSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
