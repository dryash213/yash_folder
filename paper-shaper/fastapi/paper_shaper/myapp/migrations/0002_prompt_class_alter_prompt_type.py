# Generated by Django 5.1.1 on 2024-09-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="prompt",
            name="Class",
            field=models.TextField(default="random"),
        ),
        migrations.AlterField(
            model_name="prompt",
            name="Type",
            field=models.TextField(),
        ),
    ]