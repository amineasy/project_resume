# Generated by Django 5.2 on 2025-04-10 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_dish_is_iranian_dish_discount_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='menu.menu'),
        ),
    ]
