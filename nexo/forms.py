from django import forms

from nexo.models import Saida


class SaidaForm(forms.ModelForm):
     data_vencimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )


    class Meta:
        model = Saida
        fields = "__all__"

    def clean_valor(self):
        valor = self.cleaned_data.get("valor")

        if valor <= 0:
            raise forms.ValidationError(
                "O valor da saída deve ser maior que zero."
            )

        return valor