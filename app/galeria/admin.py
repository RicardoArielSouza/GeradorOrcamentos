from django.contrib import admin
from galeria.models import *

class ListandoCategorias(admin.ModelAdmin):
    pass

admin.site.register(Categoria)
admin.site.register(Produtos)
