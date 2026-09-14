from abc import ABC, abstractmethod
from datetime import date
from .movimentacao import Movimentacao

class Entrada(Movimentacao):

    def impacto(self):
        return self.valor
        