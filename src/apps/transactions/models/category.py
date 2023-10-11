from django.db import models
from tree_queries.models import TreeNode

from mixins.models import DateTimeMixin, AuthorMixin


class TransactionCategory(DateTimeMixin, AuthorMixin, TreeNode):  # type: ignore[django-manager-missing]
    name = models.CharField(max_length=128)
    description = models.TextField()
