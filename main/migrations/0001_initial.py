# Generated by Django 4.1 on 2022-09-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Demande",
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
                ("date_demande", models.DateField(auto_now=True)),
                ("nom", models.CharField(max_length=30)),
                ("prenom", models.CharField(max_length=30)),
                ("niveau", models.CharField(max_length=30)),
                ("filiere", models.CharField(max_length=30)),
                ("for_av_eta", models.CharField(max_length=30)),
                ("for_av_fil", models.CharField(max_length=30)),
                ("interet_domaine", models.CharField(max_length=30)),
                ("interet_prolang", models.CharField(max_length=30)),
                ("parti_comp_info", models.BooleanField(default=None, null=True)),
                ("parti_comp_math", models.BooleanField(default=None, null=True)),
                ("motivation", models.CharField(max_length=500)),
                ("message", models.CharField(max_length=500)),
            ],
        ),
    ]
