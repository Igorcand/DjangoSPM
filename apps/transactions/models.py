from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.products.models import Product

class Replenishment(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    price = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    date_buy = models.DateField(null=True, blank=True)
    despesas = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    obs = models.CharField(max_length=1055, null=True, blank=True)
    total = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    # valor_total = 'CALCULADO VAI SER CALCULADO A PARTIR DO TIPO DE UNIDADE DO PRODUTO * O PREÇO POR PRODUTO * A QUANTIDADE DE PRODUTOS - DESPESAS'

    def __str__(self):
        return f'ID:{self.id}'

class Sales(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    price = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    date_sale = models.DateField(null=True, blank=True)
    discount = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    total = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    # valor_total = 'CALCULADO VAI SER CALCULADO A PARTIR DO TIPO DE UNIDADE DO PRODUTO * O PREÇO POR PRODUTO * A QUANTIDADE DE PRODUTOS - DESCONTOS'
    #PAGAMENTOS

    def __str__(self):
        return f'ID:{self.id}'




