# Generated by Django 5.1.3 on 2024-11-28 11:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='screen_size',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]