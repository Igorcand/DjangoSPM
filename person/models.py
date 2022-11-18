from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

TIPO_PESSOA = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]


class Pessoa(models.Model):
    # Dados
    nome_razao_social = models.CharField(max_length=255)
    tipo_pessoa = models.CharField(max_length=2, choices=TIPO_PESSOA)
    inscricao_municipal = models.CharField(
        max_length=32, null=True, blank=True)
    informacoes_adicionais = models.CharField(
        max_length=1055, null=True, blank=True)

    # Sobre o objeto
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_criacao = models.DateTimeField(editable=False, null=True, blank=True)
    data_edicao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome_razao_social

class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, primary_key=True, related_name='pessoa_fis_info')
    cpf = models.CharField(max_length=32, null=True, blank=True)
    rg = models.CharField(max_length=32, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.pessoa

class PessoaJuridica(models.Model):
    pessoa = models.OneToOneField(
        Pessoa, on_delete=models.CASCADE, primary_key=True, related_name='pessoa_jur_info')
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=32, null=True, blank=True)
    responsavel = models.CharField(max_length=32, null=True, blank=True)
    #sit_fiscal = models.CharField( max_length=2, null=True, blank=True, choices=ENQUADRAMENTO_FISCAL)
    suframa = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.nome_fantasia
