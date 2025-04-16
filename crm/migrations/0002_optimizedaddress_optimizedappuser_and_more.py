# Generated by Django 5.2 on 2025-04-16 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OptimizedAddress",
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
                ("street", models.CharField(max_length=255)),
                ("street_number", models.CharField(max_length=50)),
                ("city_code", models.CharField(db_index=True, max_length=20)),
                ("city", models.CharField(db_index=True, max_length=100)),
                ("country", models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="OptimizedAppUser",
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
                ("first_name", models.CharField(db_index=True, max_length=255)),
                ("last_name", models.CharField(db_index=True, max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        db_index=True,
                        max_length=1,
                    ),
                ),
                (
                    "customer_id",
                    models.CharField(db_index=True, max_length=100, unique=True),
                ),
                ("phone_number", models.CharField(db_index=True, max_length=20)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("birthday", models.DateField(db_index=True)),
                ("last_updated", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to="crm.optimizedaddress",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OptimizedCustomerRelationship",
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
                ("points", models.IntegerField(db_index=True)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("last_activity", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "appuser",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customerrelationship",
                        to="crm.optimizedappuser",
                    ),
                ),
            ],
        ),
    ]
