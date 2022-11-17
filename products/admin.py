from django.contrib import admin
from .models import Categoria, Marca, Unidade, Produto

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Unidade)
admin.site.register(Produto)
