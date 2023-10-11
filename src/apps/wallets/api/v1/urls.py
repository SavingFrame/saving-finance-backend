from rest_framework import routers

from apps.wallets.api.v1.views.group import WalletGroupViewSet
from apps.wallets.api.v1.views.wallet import WalletViewSet

router = routers.SimpleRouter()

router.register('groups', WalletGroupViewSet)
router.register('wallets', WalletViewSet)

urlpatterns = []

urlpatterns += router.urls
