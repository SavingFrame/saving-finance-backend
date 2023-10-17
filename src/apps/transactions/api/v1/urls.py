from rest_framework import routers

from apps.transactions.api.v1.views.category import TransactionCategoryViewSet

router = routers.SimpleRouter()

router.register('categories', TransactionCategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
