# Generated by Django 4.2.6 on 2023-10-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("districts", "0003_initial_values"),
    ]

    operations = [
        migrations.AlterField(
            model_name="district",
            name="name",
            field=models.CharField(
                help_text="District name", max_length=100, unique=True
            ),
        ),
    ]
