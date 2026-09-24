from django.shortcuts import render, redirect
from django.http import HttpResponse
from nexo.models import Entrada, Saida
from nexo.forms import SaidaForm
from nexo.services.movimentacoes import MovimentacaoService
from django.db.models import Q


def inicio(request):
    return HttpResponse("funcionou")


def movimentacoes_list(request):
    termo = request.GET.get("q", "")
    categoria = request.GET.get("categoria", "")

    entradas = Entrada.objects.all()
    saidas = Saida.objects.all()

    from django.db.models import Q

    filtros = Q()

    if termo:
        filtros &= Q(descricao__icontains=termo)

    if categoria:
        filtros &= Q(categoria=categoria)

    entradas = Entrada.objects.filter(filtros)
    saidas = Saida.objects.filter(filtros)

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
    
    categorias = set()

    for entrada in Entrada.objects.all():
        categorias.add(entrada.categoria)

    for saida in Saida.objects.all():
        categorias.add(saida.categoria)

    contexto = {
        "movimentacoes": movimentacoes,
        "descricoes": sorted(descricoes),
        "categorias": sorted(categorias),
    }

    return render(
        request,
        "lista.html",
        contexto,
    )

def saida_form(request):

    if request.method == "POST":
        form = SaidaForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            MovimentacaoService().registrar_saida(dados)

            return redirect("movimentacoes_list")

    else:
        form = SaidaForm()

    contexto = {
        "form": form,
    }

    return render(
        request,
        "saida_form.html",
        contexto,
    )
