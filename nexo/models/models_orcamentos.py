from django.db import models

class Orcamento(models.Model):
    conta = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )
    categoria = models.CharField(
        max_length = 200,
        null = False,
        blank = False
    )
    descricao = models.TextField(
        null = True,
        blank = True
    )
    data_registro = models.DateField()

    PERIODICIDADES = {
        "mensal": "Mensal",
        "anual": "Anual",
    }

    periodicidade = models.CharField(
        max_length=10,
        choices=PERIODICIDADES
    )

    class Meta:
        abstract = True

class LimiteDeGasto(Orcamento):
    valor_limite = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
class Meta(Orcamento):
    valor_meta = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
