from datetime import date

from nexo.dominio.movimentacoes.saida import Saida


def test_impacto_da_saida_deve_ser_negativo():
    # Arrange
    saida = Saida(
        descricao="Compra no mercado",
        valor=500,
        data_registro=date(2026, 9, 15),
        conta="Conta corrente",
        categoria="Alimentação"
    )

    # Act
    resultado = saida.impacto()

    # Assert
    assert resultado == -500

def test_saida_a_vista_deve_ter_valor_da_parcela_igual_ao_valor():
    # Arrange
    saida = Saida(
        descricao="Compra no mercado",
        valor=500,
        data_registro=date(2026, 9, 15),
        conta="Conta corrente",
        categoria="Alimentação"
    )

    # Act
    valor_parcela = saida.valor_parcela

    # Assert
    assert valor_parcela == 500

def test_saida_parcelada_deve_calcular_valor_da_parcela():
    # Arrange
    saida = Saida(
        descricao="Compra parcelada",
        valor=500,
        data_registro=date(2026, 9, 15),
        conta="Cartão",
        categoria="Eletrônicos",
        num_parcelas=5
    )

    # Act
    valor_parcela = saida.valor_parcela

    # Assert
    assert valor_parcela == 100

def test_saida_parcelada_deve_usar_valor_da_parcela_informado():
    # Arrange
    saida = Saida(
        descricao="Compra parcelada",
        valor=500,
        data_registro=date(2026, 9, 15),
        conta="Cartão",
        categoria="Eletrônicos",
        num_parcelas=5,
        valor_parcela=120
    )

    # Act
    valor_parcela = saida.valor_parcela

    # Assert
    assert valor_parcela == 120
    