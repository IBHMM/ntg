# Generated by Django 5.0.3 on 2024-12-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_ir_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
            preserve_default=False,
        ),
    ]
