# Generated by Django 5.0.1 on 2024-03-13 01:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0002_initial"),
        ("salon", "0001_initial"),
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="scheduled_date",
            new_name="date",
        ),
        migrations.AlterUniqueTogether(
            name="booking",
            unique_together={("salon", "date")},
        ),
    ]