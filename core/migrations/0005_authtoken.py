# Generated by Django 4.1.3 on 2022-12-29 20:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_student_username_alter_student_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthToken",
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
                    "value",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("issued_at", models.DateTimeField(auto_now_add=True)),
                (
                    "valid_until",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tokens",
                        to="core.student",
                    ),
                ),
            ],
        ),
    ]