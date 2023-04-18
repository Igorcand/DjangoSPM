from django.db import models

class Category(models.Model):
    categoria = models.CharField(max_length=32)
    def __str__(self):
        return self.categoria

class Brand(models.Model):
    marca = models.CharField(max_length=32)
    def __str__(self):
        return self.marca

class Unit(models.Model):
    sigla_unidade = models.CharField(max_length=3)
    unidade = models.CharField(max_length=16)

    def __str__(self):
        return self.unidade

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.PROTECT)
    unit = models.ForeignKey(
        Unit, null=True, blank=True, on_delete=models.PROTECT)
    stock = models.FloatField()
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
