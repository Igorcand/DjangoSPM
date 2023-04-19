from django.contrib import admin
from .models import Address, Email, Bank, Document, Phone

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(Address)
admin.site.register(Email, EmailAdmin)
admin.site.register(Bank)
admin.site.register(Document)
admin.site.register(Phone)

