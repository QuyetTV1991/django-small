# Generated by Django 4.2.6 on 2023-10-12 05:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pollApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="pub_data",
            new_name="pub_date",
        ),
    ]
