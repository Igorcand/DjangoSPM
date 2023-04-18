from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

PERSON_TYPE = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]

class Person(models.Model):
    nome_razao_social = models.CharField(max_length=255)
    tipo_pessoa = models.CharField(max_length=2, choices=PERSON_TYPE)

    def __str__(self):
        return self.nome_razao_social

class Physical(models.Model):
    pessoa = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=32, null=True, blank=True)
    rg = models.CharField(max_length=32, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.pessoa

class Juridical(models.Model):
    pessoa = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.nome_fantasia
