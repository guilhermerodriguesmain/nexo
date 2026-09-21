from datetime import date

from nexo.dominio.movimentacoes.parcela import Parcela


def test_impacto_da_parcela_deve_ser_negativo():
    # Arrange
    parcela = Parcela(
        descricao="Compra parcelada",
        valor=100,
        data_registro=date(2026, 9, 15),
        conta="Cartão",
        categoria="Eletrônicos",
        numero=1,
        data_vencimento=date(2026, 10, 15)
    )

    # Act
    resultado = parcela.impacto()

    # Assert
    assert resultado == -100

def test_parcela_deve_armazenar_seu_numero():
    # Arrange
    parcela = Parcela(
        descricao="Compra parcelada",
        valor=100,
        data_registro=date(2026, 9, 15),
        conta="Cartão",
        categoria="Eletrônicos",
        numero=2,
        data_vencimento=date(2026, 10, 15)
    )

    # Act
    numero = parcela.numero

    # Assert
    assert numero == 2

def test_parcela_deve_armazenar_data_de_vencimento():
    # Arrange
    data_vencimento = date(2026, 10, 15)

    parcela = Parcela(
        descricao="Compra parcelada",
        valor=100,
        data_registro=date(2026, 9, 15),
        conta="Cartão",
        categoria="Eletrônicos",
        numero=1,
        data_vencimento=data_vencimento
    )

    # Act
    resultado = parcela.data_vencimento

    # Assert
    assert resultado == data_vencimento