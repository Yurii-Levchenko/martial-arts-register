# Generated by Django 5.0 on 2023-12-13 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("martial_arts_register", "0003_martialart_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Motherland",
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
                ("name", models.CharField(max_length=50)),
                ("region", models.CharField(max_length=50)),
                ("founder", models.CharField(default="Unknown", max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="martialart",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="martialart",
            name="country_of_origin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="martial_arts_register.motherland",
            ),
        ),
    ]
