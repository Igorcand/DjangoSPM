from django.contrib import admin
from .models import Address, Email, Bank, Document, Phone

admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Bank)
admin.site.register(Document)
admin.site.register(Phone)

