from django.db import models

# Create your models here.
class Movimetacao(models.Model):
    valor = models.DecimalField(max_digits= 12, decimal_place = 2)
    data_registro = models.DateField()
    conta = models.CharField(max_legth= 100)
    categoria = models.CharField(max_length = 200)
    descricao = models.TextField()
    class Meta:
        abstract = True

class Entrada(Movimentacao):
    pass

class Saida(Movimentacao):
    pass

class Parcela(Saida):
    pass