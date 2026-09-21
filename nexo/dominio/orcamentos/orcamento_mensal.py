# nexo/dominio/orcamentos/orcamento_mensal.py

class OrcamentoMensal:

    def __init__(self, orcamento, periodo):
        self.orcamento = orcamento
        self.periodo = periodo
        self.valor = orcamento.calculo_mensal()