from .orcamento import Orcamento as orc

class Limite(orc):
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
    
    def calculo_mensal():
        
        pass

    def calculo_anual():
        pass