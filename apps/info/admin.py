from django.contrib import admin
from .models import Endereco, Email, Banco, Documento, Telefone

admin.site.register(Endereco)
admin.site.register(Email)
admin.site.register(Banco)
admin.site.register(Documento)
admin.site.register(Telefone)

# Register your models here.
