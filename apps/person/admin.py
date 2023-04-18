from django.contrib import admin
from .models import Person, Physical, Juridical

admin.site.register(Person)
admin.site.register(Physical)
admin.site.register(Juridical)

