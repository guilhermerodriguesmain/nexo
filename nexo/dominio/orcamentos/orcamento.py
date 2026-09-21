from abc import ABC, abstractmethod
from datetime import date

class Orcamento(ABC):
    def __init__(
        self,
        data_registro: date,
        conta,
        categoria,
        descricao,
        periodicidade
    ):
        self.data_registro = data_registro
        self.conta = conta
        self.categoria = categoria
        self.descricao = descricao
        self.periodicidade = periodicidade.lower()
    
    if self.periodicidade not in {"mensal", "anual"}:
    raise ValueError("Periodicidade inválida")

    @property
    @abstractmethod
    def valor(self):
        pass

    def calculo_mensal(self):
        if self.periodicidade == "anual":
            return self.valor / 12
        return self.valor

    
    def calculo_anual(self):
        if self.periodicidade == "mensal":
            return self.valor * 12
        return self.valor
