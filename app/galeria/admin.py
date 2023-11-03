from django.contrib import admin
from galeria.models import *

class ListandoCategorias(admin.ModelAdmin):
    list_display = ("id_categoria", "nome_categoria", "preco_ate_cem", "preco_ate_duzentos", "preco_acima_duzentos")
    list_display_links = ("id_categoria", "nome_categoria")
    search_fields = ("nome_categoria",)
    list_per_page = 10

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id_produto", "nome_produto", "categoria")
    list_display_links = ("id_produto", "nome_produto")
    search_fields = ("nome_produto",)
    list_filter = ("categoria",)
    list_per_page = 10

class ListandoClientes(admin.ModelAdmin):
    list_display = ("id_cliente", "nome_cliente", "e_mail")
    list_display_links = ("id_cliente", "nome_cliente")
    search_fields = ("nome_cliente",)
    list_per_page = 10

class ListandoPedidos(admin.ModelAdmin):
    list_display = ("id_pedido", "cliente", "data_pedido", "valor_total")
    list_display_links = ("id_pedido",)
    search_fields = ("id_pedido", "cliente", "data_pedido", "valor_total")
    list_filter = ("cliente", "data_pedido", "valor_total")
    list_per_page = 10

class ListandoOrcamentos(admin.ModelAdmin):
    list_display = ("id_orcamento", "cliente", "data_orcamento", "pedido")
    list_display_links = ("id_orcamento",)
    search_fields = ("id_orcamento", "cliente", "data_orcamento", "pedido")
    list_filter = ("cliente", "data_orcamento", "pedido")
    list_per_page = 10

class ListandoPedidosDetalhes(admin.ModelAdmin):
    list_display = ("id", "pedido", "produto", "valor_unitario", "quantidade")
    list_display_links = ("id", "pedido")
    search_fields = ("pedido", "produto")
    list_filter = ("pedido", "produto")
    list_per_page = 10

class ListandoOrcamentosDetalhes(admin.ModelAdmin):
    list_display = ("id", "orcamento", "produto", "valor_unitario", "quantidade")
    list_display_links = ("id", "orcamento")
    search_fields = ("orcamento", "produto")
    list_filter = ("orcamento", "produto")
    list_per_page = 10

admin.site.register(Categoria, ListandoCategorias)
admin.site.register(Produto, ListandoProdutos)
admin.site.register(Cliente, ListandoClientes)
admin.site.register(Pedido, ListandoPedidos)
admin.site.register(Orcamento, ListandoOrcamentos)
admin.site.register(PedidoDetalhe, ListandoPedidosDetalhes)
admin.site.register(OrcamentoDetalhe, ListandoOrcamentosDetalhes)
