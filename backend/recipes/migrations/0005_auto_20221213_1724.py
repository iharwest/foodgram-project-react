# Generated by Django 2.2.16 on 2022-12-13 14:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_auto_20221213_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShoppingList',
            new_name='ShoppingCart',
        ),
    ]
