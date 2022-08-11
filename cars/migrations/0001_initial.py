# Generated by Django 4.1 on 2022-08-10 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DetailType",
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
            ],
        ),
        migrations.CreateModel(
            name="Param",
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                ("value", models.CharField(max_length=50, verbose_name="Значение")),
            ],
        ),
        migrations.CreateModel(
            name="Detail",
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=11, verbose_name="Цена"
                    ),
                ),
                (
                    "amount_per_car",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Количество на одну машину"
                    ),
                ),
                (
                    "detail_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="detail_type",
                        to="cars.detailtype",
                        verbose_name="Тип детали",
                    ),
                ),
                ("params", models.ManyToManyField(to="cars.param")),
            ],
        ),
    ]
