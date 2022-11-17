from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Pagamento(models.Model):
    compra_id = models.ForeignKey(
        'compras.Compra', related_name="parcela_pagamento", on_delete=models.CASCADE)
    indice_parcela = models.IntegerField()
    vencimento = models.DateField()
    valor_parcela = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))])