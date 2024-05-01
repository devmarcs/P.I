# Generated by Django 5.0.1 on 2024-03-13 01:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "livre"),
                            (2, "ocupado"),
                            (3, "finalizado"),
                            (4, "desativo"),
                        ],
                        default=1,
                    ),
                ),
                ("commission", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Agendamento",
                "verbose_name_plural": "Agendamentos",
                "ordering": ["-created_at"],
            },
        ),
    ]