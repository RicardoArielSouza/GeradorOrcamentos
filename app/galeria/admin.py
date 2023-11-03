from django.contrib import admin
from galeria.models import *

class ListandoCategorias(admin.ModelAdmin):
    list_display = ("id_categoria", "nome_categoria", "preco_ate_cem", "preco_ate_duzentos", "preco_acima_duzentos")
    list_display_links = ("id_categoria", "nome_categoria")
    search_fields = ("nome_categoria",)
    list_per_page = 10

admin.site.register(Categoria, ListandoCategorias)
admin.site.register(Produtos)
