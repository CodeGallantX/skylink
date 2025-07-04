# Generated by Django 5.2.3 on 2025-06-23 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airline",
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
                ("code", models.CharField(max_length=2, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, upload_to="airlines/")),
            ],
        ),
        migrations.CreateModel(
            name="Airport",
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
                ("code", models.CharField(max_length=3, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
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
                ("flight_number", models.CharField(max_length=10)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                ("duration", models.DurationField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("S", "Scheduled"),
                            ("D", "Delayed"),
                            ("C", "Cancelled"),
                            ("F", "Completed"),
                        ],
                        default="S",
                        max_length=1,
                    ),
                ),
                ("economy_seats", models.PositiveIntegerField()),
                ("business_seats", models.PositiveIntegerField()),
                ("first_class_seats", models.PositiveIntegerField()),
                ("economy_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "business_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "first_class_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "airline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flights.airline",
                    ),
                ),
                (
                    "arrival_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="arrivals",
                        to="flights.airport",
                    ),
                ),
                (
                    "departure_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departures",
                        to="flights.airport",
                    ),
                ),
            ],
        ),
    ]
