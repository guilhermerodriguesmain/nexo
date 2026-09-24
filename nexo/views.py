from django.shortcuts import render
from django.http import HttpResponse
from nexo.models import Entrada, Saida
from nexo.forms import SaidaForm


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

def saida_form(request): 
    if request.method == "POST": 
        form = SaidaForm(request.POST) 

        if form.is_valid(): 
            form.save() 

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
