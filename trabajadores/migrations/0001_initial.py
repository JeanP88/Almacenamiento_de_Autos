# Generated by Django 5.1.2 on 2024-11-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trabajador",
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
                ("name", models.CharField(max_length=150)),
                ("lastName", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=200)),
                ("typeWork", models.CharField(max_length=200)),
                ("cedula", models.CharField(max_length=200)),
                ("codigo_de_empleado", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=700)),
            ],
        ),
    ]