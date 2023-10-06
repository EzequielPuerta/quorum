# Generated by Django 4.2.6 on 2023-10-04 22:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="name",
            field=models.CharField(
                default="", help_text="Party name", max_length=256, unique=True
            ),
            preserve_default=False,
        ),
    ]
