# Generated by Django 5.0 on 2023-12-31 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("martial_arts_register", "0009_embodyment_alter_artist_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="fav_technique",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="martialart",
            name="techniques",
            field=models.ManyToManyField(to="martial_arts_register.technique"),
        ),
        migrations.AlterField(
            model_name="technique",
            name="originating_martial_art",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Technique",
                to="martial_arts_register.martialart",
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="skill_level",
            field=models.CharField(
                choices=[
                    ("beginner", "Beginner"),
                    ("intermediate", "Intermediate"),
                    ("advanced", "Advanced"),
                    ("professional", "Professional"),
                ],
                default="intermediate",
                max_length=20,
            ),
        ),
    ]
