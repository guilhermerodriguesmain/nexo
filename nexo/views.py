from django.shortcuts import render
from django.http import HttpResponse
from nexo.models import Entrada, Saida

# Create your views here.
def inicio(request):
    return HttpResponse("funcionou")

def movimentacoes_list(request):
    entradas = Entrada.objects.all()
    saidas = Saida.objects.all()

    movimentacoes = [
        *entradas,
        *saidas,
    ]

    movimentacoes.sort(
        key=lambda movimentacao: movimentacao.data_registro,
        reverse=True,
    )

    contexto = {
        "movimentacoes": movimentacoes,
    }

    return render(
        request,
        "lista.html",
        contexto,
    )
