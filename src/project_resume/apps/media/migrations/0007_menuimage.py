# Generated by Django 5.2 on 2025-04-18 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_alter_branchimage_branch_alter_branchimage_image_and_more'),
        ('menu', '0010_dish_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='menu.menu')),
            ],
        ),
    ]
