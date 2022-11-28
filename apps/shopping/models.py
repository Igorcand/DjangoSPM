from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.products.models import Produto

TIPOS_DESCONTO_ESCOLHAS = (
    (u'0', u'Valor'),
    (u'1', u'Percentual'),
)


class Compra(models.Model):
    # Info
    data_emissao = models.DateField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                      MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    desconto = models.DecimalField(max_digits=15, decimal_places=4, validators=[
                                   MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    despesas = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                   MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    frete = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    seguro = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                 MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    observacoes = models.CharField(max_length=1055, null=True, blank=True)

    def __str__(self):
        return f'ID:{self.id}'


class ItensCompra(models.Model):
    produto = models.ForeignKey(Produto, related_name="compra_produto",
                                on_delete=models.CASCADE, null=True, blank=True)
    compra_id = models.ForeignKey(
        Compra, related_name="itens_compra", on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    valor_unit = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    tipo_desconto = models.CharField(
        max_length=1, choices=TIPOS_DESCONTO_ESCOLHAS, null=True, blank=True)
    desconto = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                   MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    subtotal = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                   MinValueValidator(Decimal('0.00'))], null=True, blank=True)

    def __str__(self):
        return f'{self.subtotal}'



