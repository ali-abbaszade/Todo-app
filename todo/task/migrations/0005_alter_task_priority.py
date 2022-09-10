# Generated by Django 4.1.1 on 2022-09-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0004_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[
                    (1, "High priority"),
                    (2, "Middle priority"),
                    (3, "Low priority"),
                ]
            ),
        ),
    ]
