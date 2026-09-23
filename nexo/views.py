from django.shortcuts import render
from django.http import HttpResponse
from nexo.models import Entrada, Saida


def inicio(request):
    return HttpResponse("funcionou")


def movimentacoes_list(request):
    termo = request.GET.get("q", "")

    entradas = Entrada.objects.all()
    saidas = Saida.objects.all()

    if termo:
        entradas = entradas.filter(
            descricao__icontains=termo
        )

        saidas = saidas.filter(
            descricao__icontains=termo
        )

    movimentacoes = [
        *entradas,
        *saidas,
    ]

    movimentacoes.sort(
        key=lambda movimentacao: movimentacao.data_registro,
        reverse=True,
    )

    descricoes = set()

    for entrada in Entrada.objects.all():
        descricoes.add(entrada.descricao)

    for saida in Saida.objects.all():
        descricoes.add(saida.descricao)

    contexto = {
        "movimentacoes": movimentacoes,
        "descricoes": sorted(descricoes),
    }

    return render(
        request,
        "lista.html",
        contexto,
    )
    