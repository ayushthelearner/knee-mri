# Generated by Django 5.1.4 on 2025-03-08 16:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MRIImage",
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
                ("image", models.ImageField(upload_to="uploads/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("result", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hospital",
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
                (
                    "name",
                    models.CharField(
                        default="Unknown Hospital", max_length=255, unique=True
                    ),
                ),
                ("address", models.TextField(default="Not provided")),
                ("phone_number", models.CharField(default="0000000000", max_length=15)),
                (
                    "registration_number",
                    models.CharField(default="REG123456", max_length=50, unique=True),
                ),
                ("is_verified", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hospital",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Hospital",
                "verbose_name_plural": "Hospitals",
                "ordering": ["name"],
            },
        ),
    ]
