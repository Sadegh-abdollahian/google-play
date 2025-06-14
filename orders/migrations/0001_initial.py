# Generated by Django 5.1 on 2025-06-12 09:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("applications", "0003_alter_app_icon_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_amount", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "در انتظار پرداخت"),
                            ("purchased", "پرداخت شده"),
                            ("deleted", "حذف شده"),
                        ],
                        default="draft",
                        max_length=30,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="applications.app",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
