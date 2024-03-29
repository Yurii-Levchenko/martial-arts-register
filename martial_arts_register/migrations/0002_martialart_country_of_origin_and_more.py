# Generated by Django 5.0 on 2023-12-10 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("martial_arts_register", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="martialart",
            name="country_of_origin",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="martialart",
            name="joint_locks_allowed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="martialart",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]
