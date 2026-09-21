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
        self.periodicidade = periodicidade

    @property
    @abstractmethod
    def valor():
        pass

    @abstractmethod
    def calculo_mensal(self):
        pass

    @abstractmethod
    def calculo_anual(self):
        pass
