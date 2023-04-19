from django.contrib import admin
from .models import Client, Physical, Juridical

admin.site.register(Client)
admin.site.register(Physical)
admin.site.register(Juridical)

