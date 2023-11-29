# Generated by Django 4.2.7 on 2023-11-29 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="products.subcategory",
            ),
        ),
    ]