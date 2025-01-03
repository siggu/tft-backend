# Generated by Django 5.0.2 on 2024-07-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comps", "0002_comp_is_blind"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemUsage",
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
                ("name", models.CharField(max_length=100)),
                ("usages", models.JSONField(default=dict, verbose_name="json")),
            ],
        ),
        migrations.CreateModel(
            name="MetaDecks",
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
                ("name", models.CharField(max_length=100)),
                ("decks", models.JSONField(default=dict, verbose_name="json")),
            ],
        ),
    ]
