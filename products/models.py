from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Categoria(models.Model):
    categoria_desc = models.CharField(max_length=32)

class Marca(models.Model):
    marca_desc = models.CharField(max_length=32)

class Unidade(models.Model):
    sigla_unidade = models.CharField(max_length=3)
    unidade_desc = models.CharField(max_length=16)

class Produto(models.Model):
    # Dados gerais
    codigo = models.CharField(max_length=15)
    codigo_barras = models.CharField(
        max_length=16, null=True, blank=True)  # GTIN/EAN
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.PROTECT)
    marca = models.ForeignKey(
        Marca, null=True, blank=True, on_delete=models.PROTECT)
    unidade = models.ForeignKey(
        Unidade, null=True, blank=True, on_delete=models.PROTECT)
    custo = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    venda = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)
