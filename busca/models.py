from django.db import models

class Produto(models.Model):
    codigo_do_produto = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_revenda = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_atacado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.codigo_do_produto
