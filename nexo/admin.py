from django.contrib import admin

from nexo.models import Entrada, Saida
from django import forms
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

class SaidaAdminForm(forms.ModelForm):
    data_vencimento = forms.DateField(
        required=False,
        label="Data do primeiro vencimento",
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Saida
        fields = "__all__"

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):

    form = SaidaAdminForm

    list_display = (
        "descricao",
        "valor",
        "data_registro",
        "conta",
        "categoria",
        "num_parcelas",
        "valor_parcela",
    )

    def save_model(self, request, obj, form, change):
        dados = {
            "descricao": obj.descricao,
            "valor": obj.valor,
            "data_registro": obj.data_registro,
            "conta": obj.conta,
            "categoria": obj.categoria,
            "num_parcelas": obj.num_parcelas,
            "valor_parcela": obj.valor_parcela,
            "data_vencimento": form.cleaned_data.get("data_vencimento"),
        }

        MovimentacaoService().registrar_saida(dados)
        