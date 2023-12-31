# Generated by Django 4.2.6 on 2023-10-05 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("districts", "0004_alter_district_name"),
        ("parties", "0003_initial_values"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admission",
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
                ("district_number", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admissions",
                        to="districts.district",
                    ),
                ),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admissions",
                        to="parties.party",
                    ),
                ),
            ],
        ),
    ]
