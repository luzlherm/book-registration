# Generated by Django 5.0.6 on 2024-07-17 03:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id_book",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("tittle", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("release_year", models.IntegerField()),
                ("state", models.CharField(max_length=50)),
                ("pages", models.IntegerField()),
                ("publishing_company", models.CharField(max_length=255)),
            ],
        ),
    ]
