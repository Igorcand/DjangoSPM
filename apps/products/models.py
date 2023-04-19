from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=32)
    def __str__(self):
        return self.category

class Brand(models.Model):
    brand = models.CharField(max_length=32)
    def __str__(self):
        return self.brand

class Unit(models.Model):
    acronym = models.CharField(max_length=3)
    unit = models.CharField(max_length=16)

    def __str__(self):
        return self.unit

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.PROTECT)
    unit = models.ForeignKey(
        Unit, null=True, blank=True, on_delete=models.PROTECT)
    stock = models.FloatField(default=0.0)
    add_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
