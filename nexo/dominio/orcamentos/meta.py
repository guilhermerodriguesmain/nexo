from .orcamento import Orcamento

class Acumulo(Orcamento):
    def __init__(
        self,
        data_registro,
        conta,
        categoria,
        descricao,
        periodicidade,
        valor_meta
    ):
        super()__init__(
            data_registro,
            conta,
            categoria,
            descricao,
            periodicidade
        ):

       self.valor_meta = valor_meta

    @property
    def valor(self):
        return self.valor_meta

    def calculo_mensal():
        return super().calculo_mensal()

    def calculo_anual():
        return super().calculo_anual()
        