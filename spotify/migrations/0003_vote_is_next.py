# Generated by Django 4.1.5 on 2023-01-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0002_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="vote", name="is_next", field=models.BooleanField(default=True),
        ),
    ]