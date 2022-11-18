from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from shopping.models import Compra

class Pagamento(models.Model):
    compra_id = models.ForeignKey(
        Compra, related_name="parcela_pagamento", on_delete=models.CASCADE)
    indice_parcela = models.IntegerField()
    vencimento = models.DateField()
    valor_parcela = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return f'ID:{self.id} - parcela {self.indice_parcela} = R${self.valor_parcela}'