from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=50, null=False, blank=False)
    preco_ate_cem = models.DecimalField(max_digits=10, decimal_places=2)
    preco_ate_duzentos = models.DecimalField(max_digits=10,decimal_places=2)
    preco_acima_duzentos = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nome_categoria
    
class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=50, null=False, blank=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="fotos/", blank=True)

    def __str__(self):
        return self.nome_produto
