# Generated by Django 4.2.6 on 2023-10-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pollApp", "0002_rename_pub_data_question_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(verbose_name="date published"),
        ),
    ]
