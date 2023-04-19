from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

PERSON_TYPE = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]

class Client(models.Model):
    name = models.CharField(max_length=255)
    type_client = models.CharField(max_length=2, choices=PERSON_TYPE)

    @classmethod
    def create(cls, **dict):
        client = cls(**dict)
        return client

    def __str__(self):
        return self.name

class Physical(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=32, null=True, blank=True)
    rg = models.CharField(max_length=32, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)

    @classmethod
    def create(cls, **dict):
        client = cls(**dict)
        return client

    def __str__(self):
        return self.client.name

class Juridical(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    fantasy_name = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=32, null=True, blank=True)

    @classmethod
    def create(cls, **dict):
        client = cls(**dict)
        return client

    def __str__(self):
        return self.fantasy_name
