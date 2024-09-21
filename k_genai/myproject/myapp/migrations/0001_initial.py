# Generated by Django 5.1.1 on 2024-09-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prompt",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Type", models.TextField(default="Unknown")),
                ("system_prompt", models.TextField()),
                ("prompt", models.TextField()),
                ("model", models.TextField()),
            ],
        ),
    ]
