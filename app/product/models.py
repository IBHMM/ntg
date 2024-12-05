from django.db import models

from datetime import timedelta
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Brand(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logos', blank=True, null=True)

    def __str__(self):
        return self.name


class BrandWithImage(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand_images')

    def __str__(self):
        return f'{self.name}'


class ParentCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='parent_category_images')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ManyToManyField(
        ParentCategory, related_name='categories')
    image = models.ImageField(upload_to='category_images')
    description = models.TextField(blank=True, null=True)
    filters = models.ManyToManyField('Filter')

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    name = models.CharField(models.Model)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category: {self.category}, subcategory: {self.name}'


class Filter(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class FilterValue(BaseModel):
    name = models.CharField(max_length=255)
    filter = models.ForeignKey(
        Filter, on_delete=models.CASCADE, related_name='values')

    def __str__(self):
        return f'{self.filter.name}-{self.name}'


class Product(BaseModel):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, blank=True, null=True)  # +
    model = models.CharField(max_length=255, blank=True, null=True)  # +
    link = models.URLField(blank=True, null=True)  # +
    description = models.TextField(blank=True, null=True)  # +
    poe_power_output = ArrayField(models.CharField(max_length=255))  # +
    power_consumption = ArrayField(models.CharField(max_length=255))
    poe_power_budget = ArrayField(models.CharField(max_length=255))
    poe_extend_Mode = models.CharField(max_length=255, blank=True, null=True)
    port = ArrayField(models.CharField(max_length=255))
    poe_injector_port = ArrayField(models.CharField(max_length=255))
    sfp_mini_gbic_slots = models.CharField(
        max_length=255, blank=True, null=True)
    dimensions = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    operating_temperature = models.CharField(
        max_length=255, blank=True, null=True)
    operating_humidity = models.CharField(
        max_length=255, blank=True, null=True)
    accessories = ArrayField(models.CharField(max_length=255))
    operation_mode = ArrayField(models.CharField(max_length=255))
    power_requirement = models.CharField(max_length=255, blank=True, null=True)
    max_power_consumption = models.CharField(
        max_length=255, blank=True, null=True)
    interface = ArrayField(models.CharField(max_length=255))
    frequency_band = models.CharField(max_length=255, blank=True, null=True)
    package = ArrayField(models.CharField(max_length=255))
    pixel = models.CharField(max_length=255, blank=True, null=True)
    ir_distance = ArrayField(models.CharField(max_length=255))
    power = models.CharField(max_length=255, blank=True, null=True)
    processor = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    graphics_card = models.CharField(max_length=255, blank=True, null=True)
    ssd = models.CharField(max_length=255, blank=True, null=True)
    hdd = models.CharField(max_length=255, blank=True, null=True)
    gpu = models.CharField(max_length=255, blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    camera = models.CharField(max_length=255, blank=True, null=True)
    sound = models.CharField(max_length=255, blank=True, null=True)
    guarantee = models.CharField(max_length=255, blank=True, null=True)
    operating_system = models.CharField(max_length=255, blank=True, null=True)
    compatibility = models.CharField(max_length=255, blank=True, null=True)
    resurs = models.CharField(max_length=255, blank=True, null=True)
    monitor = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    parent_category = models.ForeignKey(
        ParentCategory, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True
                                 )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.brand.name}-{self.model}'


class ProductImages(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.product.name
