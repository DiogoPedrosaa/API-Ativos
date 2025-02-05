from django.contrib import admin
from .models import Ativo, Fabricante, Tag, Setor


admin.site.register(Ativo)
admin.site.register(Fabricante)
admin.site.register(Tag)
admin.site.register(Setor)


