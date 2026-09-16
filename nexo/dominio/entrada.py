from abc import ABC, abstractmethod
from datetime import date
from .movimentacao import Movimentacao

class Entrada(Movimentacao):
    def __init__(
        self,
        descricao,
        valor,
        data,
        conta,
        categoria
    ):
        super().__init__(
            descricao,
            valor,
            data,
            conta,
            categoria
        ):

    def impacto(self):
        return self.valor
        