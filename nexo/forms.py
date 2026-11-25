from django import forms

from nexo.models import Saida


class SaidaForm(forms.ModelForm):
    # adicionar tratamento data de vencimento para que não permita ano de vencimento menor que o ano de registro

    data_vencimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )
    valor = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"step": "0.01"})
    )



    class Meta:
        model = Saida
        fields = "__all__"
        
    def clean_valor(self):
        valor = self.cleaned_data.get("valor")

        if valor is not None and valor <= 0:
            raise forms.ValidationError(
                "O valor total deve ser maior que zero."
            )

        return valor


    def clean_valor_parcela(self):
        valor_parcela = self.cleaned_data.get("valor_parcela")

        if valor_parcela is not None and valor_parcela <= 0:
            raise forms.ValidationError(
                "O valor da parcela deve ser maior que zero."
            )

        return valor_parcela

    def clean(self):
        dados = super().clean()

        valor = dados.get("valor")
        valor_parcela = dados.get("valor_parcela")
        num_parcelas = dados.get("num_parcelas")
        data_vencimento = dados.get("data_vencimento")

        if valor is None and valor_parcela is None:
            self.add_error(
                "valor",
                "Informe o valor total ou o valor da parcela."
            )

        elif valor is not None and valor_parcela is not None:
            self.add_error(
                "valor",
                "Informe apenas um dos campos: valor total ou valor da parcela."
            )

        return dados
