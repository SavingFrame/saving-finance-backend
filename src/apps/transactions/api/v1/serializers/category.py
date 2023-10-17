from rest_framework import serializers

from apps.transactions.models import TransactionCategory


class CategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ['id', 'name', 'description', 'icon', 'color', 'parent']


class SubcategorySerializer(CategoryBaseSerializer):
    pass


class TransactionCategorySerializer(CategoryBaseSerializer):
    subcategories = SubcategorySerializer(source='children', many=True, read_only=True)

    class Meta(CategoryBaseSerializer.Meta):
        model = TransactionCategory
        fields = CategoryBaseSerializer.Meta.fields + ['subcategories']
