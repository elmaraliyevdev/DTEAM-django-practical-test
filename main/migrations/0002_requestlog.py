# Generated by Django 5.1.7 on 2025-03-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestLog",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("http_method", models.CharField(max_length=10)),
                ("path", models.CharField(max_length=255)),
                ("query_string", models.TextField(blank=True, null=True)),
                ("remote_ip", models.GenericIPAddressField(blank=True, null=True)),
                ("user", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
