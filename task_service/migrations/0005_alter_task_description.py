# Generated by Django 5.0.3 on 2024-04-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_service", "0004_alter_task_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(max_length=1000),
        ),
    ]