from django.db import models

# Create your models here.
class Movimetacao(models.Model):
    valor = models.DecimalField(
        max_digits= 12, 
        decimal_place = 2
        null= False
        blank = False
    )
    data_registro = models.DateField(
        null = False, 
        blank = False
    )
    conta = models.CharField(
        max_legth= 100,
        null = False,
        blank = False
    )
    categoria = models.CharField(
        max_length = 200,
        null = False,
        Blank = False
    )
    descricao = models.TextField(
        null = True,
        blank = True
    )
    class Meta:
        abstract = True

class Entrada(Movimentacao):
    pass

class Saida(Movimentacao):
    num_parcelas = models.PositiveIntegerField(default=1)
    valor_parcela = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    

class Parcela(Movimentacao):
    saida = models.ForeignKey(
        Saida,
        on_delete=models.CASCADE,
        related_name="parcelas"
    )
    numero = models.PositiveIntegerField()
    data_vencimento = models.DateField()
    