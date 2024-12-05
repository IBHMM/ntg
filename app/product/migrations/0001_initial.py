# Generated by Django 5.0.3 on 2024-11-27 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='brand_logos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BrandWithImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='brand_images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='parent_category_images')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='category_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('parent_category', models.ManyToManyField(related_name='categories', to='product.parentcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('poe_power_output', models.CharField(blank=True, max_length=255, null=True)),
                ('power_consumption', models.CharField(blank=True, max_length=255, null=True)),
                ('poe_power_budget', models.CharField(blank=True, max_length=255, null=True)),
                ('poe_extend_Mode', models.CharField(blank=True, max_length=255, null=True)),
                ('port', models.CharField(blank=True, max_length=255, null=True)),
                ('poe_injector_port', models.CharField(blank=True, max_length=255, null=True)),
                ('sfp_mini_gbic_slots', models.CharField(blank=True, max_length=255, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
                ('operating_temperature', models.CharField(blank=True, max_length=255, null=True)),
                ('operating_humidity', models.CharField(blank=True, max_length=255, null=True)),
                ('accessories', models.TextField(blank=True, null=True)),
                ('operation_mode', models.CharField(blank=True, max_length=255, null=True)),
                ('power_requirement', models.CharField(blank=True, max_length=255, null=True)),
                ('max_power_consumption', models.CharField(blank=True, max_length=255, null=True)),
                ('interface', models.CharField(blank=True, max_length=255, null=True)),
                ('frequency_band', models.CharField(blank=True, max_length=255, null=True)),
                ('package', models.CharField(blank=True, max_length=255, null=True)),
                ('pixel', models.CharField(blank=True, max_length=255, null=True)),
                ('ir_distance', models.CharField(blank=True, max_length=255, null=True)),
                ('power', models.CharField(blank=True, max_length=255, null=True)),
                ('processor', models.CharField(blank=True, max_length=255, null=True)),
                ('ram', models.CharField(blank=True, max_length=255, null=True)),
                ('graphics_card', models.CharField(blank=True, max_length=255, null=True)),
                ('ssd', models.CharField(blank=True, max_length=255, null=True)),
                ('hdd', models.CharField(blank=True, max_length=255, null=True)),
                ('gpu', models.CharField(blank=True, max_length=255, null=True)),
                ('display', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('camera', models.CharField(blank=True, max_length=255, null=True)),
                ('sound', models.CharField(blank=True, max_length=255, null=True)),
                ('guarantee', models.CharField(blank=True, max_length=255, null=True)),
                ('operating_system', models.CharField(blank=True, max_length=255, null=True)),
                ('compatibility', models.CharField(blank=True, max_length=255, null=True)),
                ('resurs', models.CharField(blank=True, max_length=255, null=True)),
                ('monitor', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.parentcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name=models.Model)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
    ]