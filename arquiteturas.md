# arquitetura dos services 

                    SERVICES

        ┌───────────────────────────┐
        │   MovimentacaoService     │
        │                           │
View ──→│ registrar_movimentacao()  │
        │                           │
        └─────────────┬─────────────┘
                      │
             ┌────────┴────────┐
             ↓                 ↓
          Entrada             Saida
                               │
                               ↓
                            Parcela


        ┌───────────────────────────┐
        │     OrcamentoService      │
        │                           │
View ──→│ registrar_orcamento()    │
        │                           │
        └─────────────┬─────────────┘
                      ↓
                 Orcamento
                      ↓
               OrcamentoMensal

# arquitetura estrutural 

┌──────────────────────────────────────┐
│              DJANGO                 │
│                                      │
│  View        Models       HTTP        │
└───────┬───────────┬──────────────────┘
        │           │
        ↓           ↓
┌──────────────────────────────────────┐
│             SERVICES                 │
│                                      │
│  coordenação dos casos de uso        │
└──────────────────┬───────────────────┘
                   ↓
┌──────────────────────────────────────┐
│              DOMÍNIO                 │
│                                      │
│ Entrada  Saida  Parcela  Orcamento   │
└──────────────────────────────────────┘

