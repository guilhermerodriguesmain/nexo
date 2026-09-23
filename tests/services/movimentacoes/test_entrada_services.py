from datetime import date

from nexo.services.movimentacoes import MovimentacaoService

def test_registrar_entrada(db):
    # ARRANGE
    dados = {
        "descricao": "Salário",
        "valor": 5000,
        "data_registro": date(2026, 9, 23),
        "conta": "Conta corrente",
        "categoria": "Salário",
    }

    service = MovimentacaoService()

    # ACT
    entrada = service.registrar_entrada(dados)

    # ASSERT
    assert entrada.valor == 5000
    assert entrada.descricao == "Salário"