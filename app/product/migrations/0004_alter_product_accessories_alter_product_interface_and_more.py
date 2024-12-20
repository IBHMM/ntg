# Generated by Django 5.0.3 on 2024-11-28 08:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_operation_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='accessories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='interface',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='package',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='poe_injector_port',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='poe_power_budget',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='poe_power_output',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='port',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='power_consumption',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
    ]
