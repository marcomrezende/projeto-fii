# Generated by Django 4.1.1 on 2022-09-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AtivosDividendos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        db_column="id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_column="dt_created",
                        null=True,
                        verbose_name="Created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        db_column="dt_modified",
                        null=True,
                        verbose_name="Modified at",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_column="cs_active", default=True, verbose_name="Active"
                    ),
                ),
                ("ticket", models.CharField(max_length=8)),
                ("dividendo", models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                "verbose_name": "AtivosDividendos",
                "db_table": "ativos_dividendos",
            },
        ),
    ]
