# Generated by Django 4.0.6 on 2022-08-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_size_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='product_size', to='shop.sizevariants'),
        ),
    ]
