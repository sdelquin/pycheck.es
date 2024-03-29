# Generated by Django 4.1.3 on 2023-01-04 19:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_student_password_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submission",
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
                ("passed", models.BooleanField(default=False)),
                ("body", models.TextField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="submissions",
                        to="core.exercise",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="submissions",
                        to="core.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deadline",
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
                ("closed_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="deadlines",
                        to="core.context",
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="deadlines",
                        to="core.exercise",
                    ),
                ),
            ],
        ),
    ]
