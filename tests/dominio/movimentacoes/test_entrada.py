from datetime import date

from nexo.dominio.movimentacoes.entrada import Entrada


def test_impacto_da_entrada_deve_ser_positivo():
    # Arrange
    entrada = Entrada(
        descricao="Salário",
        valor=3000,
        data_registro=date(2026, 9, 15),
        conta="Conta corrente",
        categoria="Salário"
    )

    # Act
    resultado = entrada.impacto()

    # Assert
    assert resultado == 3000

def test_impacto_da_entrada_deve_ser_positivo():
    entrada = Entrada(
        descricao="Salário",
        valor=3000,
        data_registro=date(2026, 9, 15),
        conta="Conta corrente",
        categoria="Salário"
    )

    resultado = entrada.impacto()

    assert resultado == 3000

def test_impacto_da_entrada_deve_corresponder_ao_valor():
    entrada = Entrada(
        descricao="Freelance",
        valor=750,
        data_registro=date(2026, 9, 15),
        conta="Conta corrente",
        categoria="Serviços"
    )

    resultado = entrada.impacto()

    assert resultado == 750