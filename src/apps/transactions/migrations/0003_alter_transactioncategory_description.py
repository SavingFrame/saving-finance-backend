# Generated by Django 4.2.6 on 2023-10-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transactioncategory_color_transactioncategory_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactioncategory',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
