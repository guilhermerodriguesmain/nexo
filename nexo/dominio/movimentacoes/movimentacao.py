from abc import ABC, abstractmethod
from datetime import date

class Movimentacao(ABC):
    def __init__(self,
    descricao,
    valor,
    data_registro,
    conta,
    categoria
    ):
    
    self.descricao = descricao : str
    self.valor = valor
    self.data_registro = data_registro
    self.conta = conta
    self.categoria = categoria

    @abstractmethod
    def impacto(self):
        pass

