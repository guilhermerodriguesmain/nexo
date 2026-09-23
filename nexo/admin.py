from django.contrib import admin

from nexo.models import Entrada
from nexo.services.movimentacoes import MovimentacaoService


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):

    list_display = (
        "descricao",
        "valor",
        "data_registro",
        "conta",
        "categoria",
    )

    def save_model(self, request, obj, form, change):
        dados = {
            "descricao": obj.descricao,
            "valor": obj.valor,
            "data_registro": obj.data_registro,
            "conta": obj.conta,
            "categoria": obj.categoria,
        }

        MovimentacaoService().registrar_entrada(dados)
