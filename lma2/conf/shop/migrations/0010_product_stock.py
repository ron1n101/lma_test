# Generated by Django 4.0.6 on 2022-08-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_productsize_options_remove_product_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]
