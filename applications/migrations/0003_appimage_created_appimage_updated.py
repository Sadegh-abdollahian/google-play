# Generated by Django 5.2 on 2025-07-10 14:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0002_category_created_category_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="appimage",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appimage",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
