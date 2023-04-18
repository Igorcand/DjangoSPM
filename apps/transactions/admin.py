from django.contrib import admin
from .models import Compra, ItensCompra

class ItensCompraInLine(admin.TabularInline):
    model = ItensCompra
    extra = 1


class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInLine]

admin.site.register(Compra, CompraAdmin)
admin.site.register(ItensCompra)
