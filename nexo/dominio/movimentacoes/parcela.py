
from datetime import date
from .saida import Saida

class Parcela(Saida):
    def __init__(
        self,
        numero,
        valor,
        data_vencimento,
        data_registro,
        conta,
        categoria,
        descricao
    ):
        super().__init__(
            data_registro = data_registro,
            conta = conta,
            valor = valor,
            categoria = categoria,
            descricao = descricao
        )
        
        self.numero = numero
        self.valor = self.valor_parcela
        self.data_vencimento = data_vencimento

    """
    implementar

    def impacto():
        return - self.valor

    se torna mera ferramenta semantica por que como saida.impacto() ja renorna -self.valor
    quando mudarmos o contexo para parcela.impacto() o metodo vai procurar o atributo self.valor 
    de parcela não o atributo valor de saida
    """
    