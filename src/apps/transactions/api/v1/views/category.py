from rest_framework import viewsets

from apps.transactions.models import TransactionCategory
from apps.transactions.api.v1.serializers import category as serializers


class TransactionCategoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all()
    serializer_class = serializers.TransactionCategorySerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user, parent=None)
