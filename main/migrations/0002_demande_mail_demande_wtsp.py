# Generated by Django 4.1 on 2022-09-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="demande",
            name="mail",
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name="demande",
            name="wtsp",
            field=models.CharField(default=None, max_length=30),
        ),
    ]
