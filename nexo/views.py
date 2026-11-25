from django.shortcuts import render, redirect
from django.http import HttpResponse
from nexo.models import Entrada, Saida
from nexo.forms import SaidaForm
from nexo.services.movimentacoes import MovimentacaoService
from django.db.models import Q


def inicio(request):
    return HttpResponse("funcionou")


def movimentacoes_list(request):
    service = MovimentacaoService()

    movimentacoes = service.listar_movimentacoes(
        termo=request.GET.get("q", ""),
        categoria=request.GET.get("categoria", ""),
    )

    opcoes = service.obter_opcoes_filtro()

    contexto = {
        "movimentacoes": movimentacoes,
        "descricoes": opcoes["descricoes"],
        "categorias": opcoes["categorias"],
    }

    return render(request, "lista.html", contexto)

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
