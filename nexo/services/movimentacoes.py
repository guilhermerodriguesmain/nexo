from calendar import monthrange

from nexo.dominio.movimentacoes.entrada import Entrada
from nexo.dominio.movimentacoes.saida import Saida
from nexo.dominio.movimentacoes.parcela import Parcela

from nexo.models import Entrada as EntradaModel
from nexo.models import Saida as SaidaModel
from nexo.models import Parcela as ParcelaModel


class MovimentacaoService:

    def registrar_entrada(self, dados):
        entrada = Entrada(
            descricao=dados["descricao"],
            valor=dados["valor"],
            data_registro=dados["data_registro"],
            conta=dados["conta"],
            categoria=dados["categoria"],
        )

        return EntradaModel.objects.create(
            descricao=entrada.descricao,
            valor=entrada.valor,
            data_registro=entrada.data_registro,
            conta=entrada.conta,
            categoria=entrada.categoria,
        )

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

        saida_model = SaidaModel.objects.create(
            descricao=saida.descricao,
            valor=saida.valor,
            data_registro=saida.data_registro,
            conta=saida.conta,
            categoria=saida.categoria,
            num_parcelas=saida.num_parcelas,
            valor_parcela=saida.valor_parcela,
        )

        if saida.num_parcelas > 1:
            self._gerar_parcelas(
                saida,
                saida_model,
                dados["data_vencimento"],
            )

        return saida_model

    def listar_movimentacoes(self, termo_busca=None, categoria=None):
        movimentacoes = []

        entradas = EntradaModel.objects.all()
        saidas = SaidaModel.objects.all()

        if termo_busca:
            entradas = entradas.filter(descricao__icontains=termo_busca)
            saidas = saidas.filter(descricao__icontains=termo_busca)

        if categoria:
            entradas = entradas.filter(categoria=categoria)
            saidas = saidas.filter(categoria=categoria)

        for entrada in entradas:
            movimentacoes.append(entrada)

        for saida in saidas:
            movimentacoes.append(saida)

        return movimentacoes
    
    def opcoes_filtro(self):
        descricoes = set()
        categorias = set()

        for entrada in EntradaModel.objects.all():
            descricoes.add(entrada.descricao)
            categorias.add(entrada.categoria)

        for saida in SaidaModel.objects.all():
            descricoes.add(saida.descricao)
            categorias.add(saida.categoria)

        return {
            "descricoes": sorted(descricoes),
            "categorias": sorted(categorias),
        }

    def _gerar_parcelas(
        self,
        saida,
        saida_model,
        data_vencimento_inicial,
    ):
        for numero in range(1, saida.num_parcelas + 1):

            data_vencimento = self._adicionar_meses(
                data_vencimento_inicial,
                numero - 1,
            )

            parcela = Parcela(
                numero=numero,
                valor=saida.valor_parcela,
                data_vencimento=data_vencimento,
                data_registro=saida.data_registro,
                conta=saida.conta,
                categoria=saida.categoria,
                descricao=saida.descricao,
            )

            ParcelaModel.objects.create(
                saida=saida_model,
                numero=parcela.numero,
                valor=parcela.valor,
                data_vencimento=parcela.data_vencimento,
                data_registro=parcela.data_registro,
                conta=parcela.conta,
                categoria=parcela.categoria,
                descricao=parcela.descricao,
            )

    def _adicionar_meses(self, data, meses):
        mes = data.month - 1 + meses
        ano = data.year + mes // 12
        mes = mes % 12 + 1

        dia = min(
            data.day,
            monthrange(ano, mes)[1],
        )

        return data.replace(
            year=ano,
            month=mes,
            day=dia,
        )
        