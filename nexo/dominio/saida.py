from abc import ABC, abstractmethod
from datetime import date
from .movimentacao import Movimentacao

class Saida(Movimentacao):
    #sugestão: adicionar lógica para retornar impacto equivalente a parcela do mes
    #sugestão: adicionar lógica para retornar n° parcelas contando que a primeira parcela é ja no mês atual portanto num_parcelas : num_parcelas -1 ou podemos tratar em parcela.py quando podemos fazer a verificação de datetime para saber qual o mes atual e implentar logica de parcelas restantes
    def __init__(
        self,
        descricao = None,
        valor,
        data,
        conta,
        categoria
        num_parcelas = 1
        valor_parcelas 
    ):
        super().__init__(
            descricao,
            valor,
            data,
            conta,
            categoria
        ):

        self.num_parcelas = num_parcelas
        self.valor_parcelas = valor_parcelas

    def impacto(self):
        return - self.valor


    def parcelar_por_valor(self, valor_total:float, num_parcelas:int = 1):
        # usar quando por ex: 500 divididos em 5 parcelas
        self.num_parcelas = num_parcelas
        self.valor = valor_total

        if num_parcelas > 1 and (self.valor_parcela is None):
             self.valor_parcelas =  valor_total / num_parcelas
        else:
             self.valor_parcelas =  valor_total 


    def parcelar_por_quantidade(self, valor_parcelas:float, num_parcelas:int = 1):
        #usar quando por ex: 5 parcelas de 100
        
        self.valor_parcelas =  valor_parcelas 
        self.num_parcelas = num_parcelas
        
        if num_parcelas > 1 :
             self.valor = valor_parcelas * num_parcelas
        else:
             self.valor = valor_parcelas