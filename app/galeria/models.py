from django.db import models
from datetime import datetime

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=50, null=False, blank=False)
    preco_ate_cem = models.DecimalField(max_digits=10, decimal_places=2)
    preco_ate_duzentos = models.DecimalField(max_digits=10,decimal_places=2)
    preco_acima_duzentos = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nome_categoria
    
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="fotos/", blank=True)

    def __str__(self):
        return self.nome_produto

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=150, null=False, blank=False)
    e_mail = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome_cliente
    
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_pedido = models.DateField(default=datetime.now, blank=False)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id_pedido)

class Orcamento(models.Model):
    id_orcamento = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_orcamento = models.DateField(default=datetime.now, blank=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id_orcamento)
    
class PedidoDetalhe(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self.id)

class OrcamentoDetalhe(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self.id)