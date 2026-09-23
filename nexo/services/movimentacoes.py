from nexo.dominio.movimentacoes.entrada import Entrada
from nexo.models import Entrada as EntradaModel


class MovimentacaoService:

    def registrar_entrada(self, dados):
        entrada = Entrada(
            descricao=dados["descricao"],
            valor=dados["valor"],
            data_registro=dados["data_registro"],
            conta=dados["conta"],
            categoria=dados["categoria"]
        )

        entrada_model = EntradaModel.objects.create(
            descricao=entrada.descricao,
            valor=entrada.valor,
            data_registro=entrada.data_registro,
            conta=entrada.conta,
            categoria=entrada.categoria
        )

        return entrada_model

    def registrar_saida(self, dados):
        saida = Saida(
            descricao=dados["descricao"],
            valor=dados["valor"],
            data_registro=dados["data_registro"],
            conta=dados["conta"],
            categoria=dados["categoria"],
            num_parcelas=dados.get("num_parcelas", 1),
            valor_parcela=dados.get("valor_parcela"),
        )

        return SaidaModel.objects.create(
            descricao=saida.descricao,
            valor=saida.valor,
            data_registro=saida.data_registro,
            conta=saida.conta,
            categoria=saida.categoria,
            num_parcelas=saida.num_parcelas,
            valor_parcela=saida.valor_parcela,
        )