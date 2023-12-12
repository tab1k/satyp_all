# Generated by Django 4.2.7 on 2023-12-12 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_customuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_verified_email",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="EmailVerification",
            fields=[
                (
                    "code",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("expiration", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]