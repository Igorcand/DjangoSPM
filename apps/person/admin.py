from django.contrib import admin
from .models import Pessoa, PessoaFisica, PessoaJuridica

admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)

