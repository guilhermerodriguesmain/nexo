from abc import ABC, abstractmethod
from datetime import date
from .movimentacao import Movimentacao

class Saida(Movimentacao):
    #sugestão: adicionar lógica para retornar impacto equivalente a parcela do mes
    #sugestão: adicionar lógica para retornar n° parcelas contando que a primeira parcela é ja no mês atual portanto num_parcelas : num_parcelas -1 ou podemos tratar em parcela.py quando podemos fazer a verificação de datetime para saber qual o mes atual e implentar logica de parcelas restantes
    def __init__(
        self,
        descricao,
        valor,
        data,
        conta,
        categoria,
        num_parcelas = 1,
        valor_parcela = none
    ):
        super().__init__(
            descricao,
            valor,
            data,
            conta,
            categoria
        )

        self.num_parcelas = num_parcela
        self.valor_parcela = valor_parcela

        if (valor_parcela is None) and (num_parcelas == 1):
            # compra a vista
            self.valor_parcela = valor
        elif (valor_parcela is None) and (num_parcelas > 1):
            # calcular parcelas a partir do valor total
            self._parcelar_por_valor(valor, num_parcelas)
        else:
            # tenho valor da parcela e quero calcular o valor total a partir do valor das parcelas e sua quantidade
            self._parcelar_por_quantidade(valor_parcela, num_parcelas)


    def impacto(self):
        return - self.valor


    def _parcelar_por_valor(self, valor_total:float, num_parcelas:int = 1):
        # usar quando por ex: 500 divididos em 5 parcelas
        self.valor_parcela =  valor_total / num_parcelas
        self.num_parcelas = num_parcelas
        self.valor = valor_total

    def _parcelar_por_quantidade(self, valor_parcela:float, num_parcelas:int = 1):
        #usar quando por ex: 5 parcelas de 100
        self.valor_parcela =  valor_parcela 
        self.num_parcelas = num_parcelas
        self.valor = valor_parcela * num_parcelas
        