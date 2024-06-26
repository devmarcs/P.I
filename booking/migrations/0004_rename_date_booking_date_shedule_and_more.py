# Generated by Django 5.0.1 on 2024-03-15 04:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0003_rename_scheduled_date_booking_date_and_more"),
        ("salon", "0001_initial"),
        ("schedule", "0002_alter_schedule_collaborator_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="date",
            new_name="date_shedule",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="service",
            new_name="services",
        ),
        migrations.AlterUniqueTogether(
            name="booking",
            unique_together={("salon", "date_shedule")},
        ),
        migrations.AddField(
            model_name="booking",
            name="end_booking",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="start_booking",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="booking",
            name="time_required",
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
