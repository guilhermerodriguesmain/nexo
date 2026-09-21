from .orcamento import Orcamento as orc

class LimiteDeGasto(orc):
    def __init__(
        self,
        data_registro,
        conta,
        categoria,
        descricao,
        periodicidade,
        valor_limite
    ):
        super()__init__(
            data_registro,
            conta,
            categoria,
            descricao,
            periodicidade
        ):

       self.valor_limite = valor_limite

    @property
    def valor(self):
        return self.valor_limite
    
    def calculo_mensal(self):
        return super().calculo_mensal()

    def calculo_anual(self):
        return super().calculo_anual()