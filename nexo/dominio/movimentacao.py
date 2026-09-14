from abc import ABC, abstractmethod
from datetime import date

class Movimentacao(ABC):
    def __init__(self,
    descricao,
    valor,
    data,
    conta,
    categoria
    ):
    
    self.descricao = descricao
    self.valor = valor
    self.data = data
    self.conta = conta
    self.categoria = categoria

    @abstractmethod

    def impacto(self):
        pass
    
