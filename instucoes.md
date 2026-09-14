# Controle Financeiro — Arquitetura e Fluxo de Trabalho

## 1. Visão geral

Este documento registra as decisões arquiteturais e o fluxo de desenvolvimento definidos para o projeto **Controle Financeiro — Orçamento por categoria e parcelamento automático**.

O objetivo é manter o núcleo da aplicação organizado em torno das regras do negócio, evitando que o Django, o banco de dados ou futuras integrações externas ditem a modelagem do domínio.

O projeto será desenvolvido em duas entregas principais:

- **P1 — Entrega 1:** movimentações financeiras, orçamento por categoria/mês e parcelamento.
- **P2 — Entrega 2:** múltiplos espaços, papéis, dashboard e API.

Integrações bancárias e Open Finance ficam para uma etapa futura.

---

# 2. Princípios arquiteturais

## 2.1 Domínio independente do Django

As regras centrais do negócio serão implementadas em Python puro.

O diretório `dominio/` **não deve depender de Django**.

Isso permite:

- testar as regras sem banco de dados;
- testar sem subir o Django;
- reutilizar as regras em outros contextos;
- evitar que o ORM determine a estrutura do domínio;
- facilitar futuras integrações, como Open Finance.

A separação conceitual é:

```text
Request
   ↓
View
   ↓
Service (quando necessário)
   ↓
Domínio
   ↓
Persistência
```

A view recebe a requisição e coordena a interface HTTP.

O service coordena operações que envolvem vários objetos.

O domínio concentra os conceitos e regras do negócio.

A persistência fica sob responsabilidade dos models/Django ORM.

---

# 3. Domínio não é banco de dados

Uma decisão importante é não tratar o diretório `dominio/` como uma representação do banco.

## Domínio

Representa:

- o que é uma movimentação;
- o que é uma entrada;
- o que é uma saída;
- como uma saída pode ser parcelada;
- o que é uma parcela;
- o que é uma conta;
- o que é uma categoria;
- o que é um orçamento;
- como as regras financeiras funcionam.

## Models

Representam:

- como esses dados serão persistidos;
- tabelas;
- relacionamentos do ORM;
- chaves;
- índices;
- constraints de banco;
- detalhes específicos do Django.

Portanto, a pergunta para o domínio é:

> "Como o negócio funciona?"

Enquanto a pergunta para os models é:

> "Como os dados serão armazenados?"

---

# 4. Regra para criação de Services

Não serão criados services apenas para seguir um padrão arquitetural.

A regra adotada é:

> Se o comportamento pertence claramente a um objeto, ele deve ficar no objeto.

Exemplo:

```python
saida.parcelar(...)
```

O parcelamento pertence naturalmente a uma `Saida`.

Por outro lado:

> Se uma operação precisa coordenar vários objetos ou etapas do sistema, pode ser criado um service.

Exemplo futuro:

```text
registrar uma saída
        ↓
criar a movimentação
        ↓
atualizar/persistir conta
        ↓
associar categoria
        ↓
gerar parcelas
        ↓
persistir tudo
```

Esse tipo de operação pode justificar um service.

---

# 5. Estrutura de diretórios

A estrutura inicial será pequena e deliberadamente simples:

```text
controle-financeiro/
│
├── financeiro/
│   │
│   ├── dominio/
│   │   ├── __init__.py
│   │   ├── movimentacao.py
│   │   ├── entrada.py
│   │   ├── saida.py
│   │   ├── parcela.py
│   │   ├── conta.py
│   │   ├── categoria.py
│   │   └── orcamento.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── views/
│   │   └── __init__.py
│   │
│   └── ...
│
├── tests/
│   ├── dominio/
│   └── services/
│
├── manage.py
└── ...
```

A estrutura poderá crescer conforme o projeto precisar, mas não serão criados diretórios ou abstrações antecipadamente.

A prioridade é manter imports simples e reduzir a possibilidade de problemas como `ModuleNotFoundError`.

---

# 6. Responsabilidade de cada diretório

## `financeiro/dominio/`

Contém as classes e regras de negócio.

Características:

- Python puro;
- sem dependência do Django;
- sem acesso direto ao banco;
- foco em comportamento e invariantes do negócio.

## `financeiro/services/`

Contém operações que coordenam múltiplos objetos ou etapas do domínio.

Não deve conter regras que pertencem claramente a uma entidade/objeto.

## `financeiro/models/`

Contém a camada de persistência.

Responsabilidades:

- Django ORM;
- relacionamento entre registros;
- persistência;
- constraints;
- mapeamento para banco.

## `financeiro/views/`

Contém a interface HTTP.

Responsabilidades:

- receber request;
- validar aspectos da requisição;
- chamar services/domínio;
- devolver response.

A view não deve concentrar regras financeiras complexas.

## `tests/`

Contém os testes automatizados.

A prioridade inicial será testar o domínio antes de construir toda a camada Django.

---

# 7. Modelagem do domínio

A hierarquia principal definida é:

```text
Movimentacao <<abstract>>
    ▲
    │
 ┌──┴───┐
 │      │
Entrada Saida
          │
          ◆
          │
       Parcela
```

As relações complementares:

```text
Conta ─── 1:N ─── Movimentacao

Categoria ─── 1:N ─── Movimentacao

Categoria ◆── Orcamento
```

---

# 8. `Movimentacao`

`Movimentacao` será uma classe abstrata.

Ela representa aquilo que é comum a qualquer movimento financeiro.

## Atributos

Inicialmente:

```text
id
descricao
valor
data
conta
categoria
```

## Método

```python
impacto()
```

O método será abstrato.

A responsabilidade é informar o impacto financeiro da movimentação.

Regra:

```text
Entrada → impacto positivo
Saida   → impacto negativo
```

---

# 9. `Entrada`

`Entrada` herda de `Movimentacao`.

Representa dinheiro entrando no sistema financeiro.

Exemplos:

- salário;
- freelance;
- reembolso;
- venda;
- rendimento.

## Método

```python
impacto()
```

Retorna o valor da entrada como positivo.

Não serão criados métodos artificiais sem necessidade real do domínio.

---

# 10. `Saida`

`Saida` herda de `Movimentacao`.

Representa dinheiro saindo.

Exemplos:

- mercado;
- aluguel;
- restaurante;
- notebook;
- assinatura.

## Métodos definidos inicialmente

```python
impacto()
parcelar()
```

### `impacto()`

Retorna o valor da saída como negativo.

### `parcelar()`

Responsável por gerar as parcelas de uma saída.

O método deverá suportar dois modos de entrada:

### Modo A — valor total

O usuário informa:

```text
valor total
número de parcelas
```

Exemplo:

```text
R$ 3.000
10 parcelas
```

Resultado:

```text
10 × R$ 300
```

### Modo B — valor da parcela

O usuário informa:

```text
valor da parcela
número de parcelas
```

Exemplo:

```text
R$ 300 por parcela
10 parcelas
```

Resultado:

```text
valor total = R$ 3.000
```

As regras exatas da assinatura do método ainda serão fechadas antes da implementação.

---

# 11. `Parcela`

`Parcela` foi definida como um objeto pertencente a uma `Saida`.

Ela **não será tratada como uma entidade independente do lançamento**.

A relação conceitual é:

```text
Saida ◆── 0..N Parcela
```

Isso representa composição:

> Uma parcela existe porque existe uma saída que a originou.

## Atributos

Inicialmente:

```text
numero
valor
data
```

Não haverá duplicação desnecessária de informações como:

- descrição;
- conta;
- categoria.

Essas informações pertencem à `Saida`.

Exemplo:

```text
Saida
  Notebook
  R$ 3.000
  10x
      ├── Parcela 1: R$ 300 — setembro
      ├── Parcela 2: R$ 300 — outubro
      ├── Parcela 3: R$ 300 — novembro
      └── ...
```

---

# 12. `Conta`

`Conta` representa o meio ou local financeiro onde a movimentação ocorre.

Exemplos:

- Nubank;
- Itaú;
- carteira;
- cartão.

## Atributos

Inicialmente:

```text
id
nome
```

Nenhum método obrigatório foi definido neste momento.

Também não será assumido que `saldo` precise ser armazenado como atributo.

O saldo poderá ser derivado das movimentações:

```text
saldo = entradas - saídas
```

Essa decisão poderá ser refinada quando a persistência for implementada.

---

# 13. `Categoria`

`Categoria` classifica as movimentações.

Exemplos:

- Alimentação;
- Transporte;
- Moradia;
- Lazer;
- Salário;
- Eletrônicos.

## Atributos

Inicialmente:

```text
id
nome
```

Foi definida a possibilidade de a categoria possuir seus orçamentos.

Conceitualmente:

```text
Categoria
 ├── Orçamento Setembro
 ├── Orçamento Outubro
 └── Orçamento Novembro
```

Isso caracteriza uma relação de composição entre categoria e seus orçamentos.

Os métodos exatos, como `adicionar_orcamento()` e `obter_orcamento()`, ainda serão definidos antes da implementação.

---

# 14. `Orcamento`

`Orcamento` representa o limite planejado de uma categoria em determinado mês.

## Atributos conceituais

```text
categoria
mes
ano
valor
```

Exemplo:

```text
Categoria: Alimentação
Mês: setembro
Ano: 2026
Limite: R$ 1.000
```

## Gasto realizado

Inicialmente, não será armazenado um atributo `gasto`.

O gasto pode ser calculado a partir das movimentações e parcelas pertencentes à categoria naquele período.

Exemplo:

```text
Orçamento: R$ 1.000

Gastos no mês:
    R$ 200
    R$ 150
    R$ 50

Realizado: R$ 400
Disponível: R$ 600
```

Isso evita duplicar uma informação que pode ser derivada dos lançamentos.

Métodos como:

```python
disponivel()
```

e eventualmente outros comportamentos do orçamento ainda serão definidos.

---

# 15. Regras de orçamento

O orçamento é definido por:

```text
categoria + mês + ano
```

Exemplo:

```text
Alimentação + setembro/2026
```

Uma movimentação de saída ou uma parcela pertencente àquela categoria e mês afeta o orçamento correspondente.

Entradas não consomem orçamento de despesas.

Portanto:

```text
Entradas → resultado financeiro
Saídas   → orçamento de despesas
```

O resultado financeiro pode ser representado por:

```text
resultado = entradas - saídas
```

---

# 16. Regra de parcelamento e orçamento

Uma compra parcelada não deve consumir todo o orçamento no mês da compra.

Exemplo:

```text
Notebook: R$ 3.000
10 parcelas de R$ 300
```

Distribuição:

```text
Setembro   → R$ 300
Outubro    → R$ 300
Novembro   → R$ 300
Dezembro   → R$ 300
...
```

Cada parcela impacta o orçamento da categoria no mês correspondente.

Assim:

```text
Orçamento de Eletrônicos — setembro
    ↓
    Parcela 1 = R$ 300

Orçamento de Eletrônicos — outubro
    ↓
    Parcela 2 = R$ 300
```

A compra original continua sendo uma única `Saida`, mas seus efeitos financeiros mensais são representados pelas `Parcela`.

---

# 17. Datas das parcelas

A distribuição das parcelas deverá considerar os meses subsequentes ao lançamento.

Exemplo:

```text
Compra: 15/09/2026
10 parcelas

Parcela 1 → setembro/2026
Parcela 2 → outubro/2026
Parcela 3 → novembro/2026
...
```

As regras exatas para situações como:

- compra no dia 31;
- fevereiro;
- meses com quantidades diferentes de dias;

ainda deverão ser definidas antes da implementação.

---

# 18. Arredondamento de valores

O parcelamento exige uma regra explícita para valores que não dividem exatamente.

Exemplo:

```text
R$ 100 / 3 parcelas
```

Não é possível representar exatamente:

```text
33,333...
```

em centavos.

Portanto, antes da implementação de `Saida.parcelar()`, deverá ser definida uma política de arredondamento, provavelmente distribuindo o restante de centavos entre as primeiras ou últimas parcelas.

Essa regra será tratada como uma invariante do domínio.

---

# 19. Invariantes a definir antes da implementação

Antes de escrever as classes definitivamente, deverão ser fechadas as seguintes regras.

## Valores

- valores monetários devem ser válidos;
- definir representação monetária;
- impedir valores incompatíveis com a operação;
- definir regra de arredondamento.

## Parcelamento

- número de parcelas deve ser válido;
- definir comportamento para uma parcela;
- impedir quantidade inválida de parcelas;
- definir exatamente quando `valor_total` ou `valor_parcela` pode ser informado;
- evitar informar simultaneamente dados conflitantes;
- garantir que a soma das parcelas corresponda ao total.

## Datas

- definir data da primeira parcela;
- definir avanço entre meses;
- definir comportamento para dias inexistentes nos meses seguintes.

## Orçamento

- definir se pode existir mais de um orçamento para a mesma categoria/mês/ano;
- definir comportamento ao tentar criar um orçamento duplicado;
- definir regras para orçamento inexistente.

Essas decisões serão tomadas antes da implementação dos objetos.

---

# 20. Fluxo funcional da P1

O fluxo geral da primeira entrega será:

```text
Usuário
   ↓
Cadastro de conta
   ↓
Cadastro de categoria
   ↓
Cadastro de movimentação
   ↓
Entrada ou Saída
   ↓
Se for Saída:
   ├── à vista
   └── parcelada
          ↓
       Parcelas
          ↓
   Distribuição por mês
          ↓
   Impacto no orçamento
```

---

# 21. Fluxo de uma saída à vista

Exemplo:

```text
Categoria: Alimentação
Conta: Nubank
Valor: R$ 200
Data: 10/09/2026
```

Fluxo:

```text
Usuário
   ↓
View
   ↓
Domínio
   ↓
Saida
   ↓
Impacto = -R$ 200
   ↓
Orçamento Alimentação/09-2026
   ↓
Realizado += R$ 200
```

---

# 22. Fluxo de uma saída parcelada

Exemplo:

```text
Notebook
R$ 3.000
10 parcelas
```

Fluxo:

```text
Usuário
   ↓
View
   ↓
Saida
   ↓
Saida.parcelar()
   ↓
10 Parcelas
   ↓
Cada parcela recebe sua data
   ↓
Cada mês recebe o impacto correspondente
   ↓
Orçamento da categoria é afetado mês a mês
```

---

# 23. Futuras integrações

O domínio não deverá conhecer a origem da movimentação.

Hoje:

```text
Usuário
   ↓
Formulário
   ↓
Movimentacao
```

No futuro:

```text
Banco / Open Finance
   ↓
Adapter
   ↓
Movimentacao
```

O domínio continua trabalhando com:

```text
Entrada
Saida
Conta
Categoria
Parcela
Orcamento
```

sem precisar conhecer detalhes de APIs bancárias.

Isso permite adicionar integrações sem reescrever as regras centrais do negócio.

---

# 24. Escopo da P1

A P1 terá como objetivo permitir:

- cadastro de contas;
- cadastro de categorias;
- cadastro de entradas;
- cadastro de saídas;
- orçamento por categoria/mês;
- saídas à vista;
- saídas parceladas;
- parcelamento por valor total;
- parcelamento por valor da parcela;
- cálculo automático do valor ausente;
- geração das parcelas;
- distribuição das parcelas pelos meses;
- associação das parcelas à categoria;
- acompanhamento de orçamento x realizado.

---

# 25. Fora do escopo da P1

Não fazem parte da primeira entrega:

- múltiplos espaços;
- papéis;
- permissões;
- dashboard;
- API pública;
- integrações externas;
- importação automática de extratos;
- Open Finance;
- categorização automática;
- sincronização bancária.

Esses recursos poderão entrar na P2 ou em versões posteriores.

---

# 26. P2

A segunda entrega deverá evoluir o sistema para suportar:

- múltiplos espaços;
- diferentes papéis;
- permissões;
- dashboard;
- API.

A P2 será construída sobre o domínio desenvolvido na P1, evitando reescrever as regras financeiras fundamentais.

---

# 27. Fluxo de desenvolvimento

A ordem de implementação definida é:

```text
1. Definir domínio
       ↓
2. Definir atributos
       ↓
3. Definir invariantes
       ↓
4. Definir métodos
       ↓
5. Implementar domínio puro
       ↓
6. Criar testes do domínio
       ↓
7. Criar Models Django
       ↓
8. Criar Services necessários
       ↓
9. Criar Views
       ↓
10. Integrar interface
```

A ideia é evitar começar diretamente pelo `models.py`.

---

# 28. Etapa 1 — Fechar o domínio

Antes de implementar, devem ser fechados:

- atributos;
- tipos;
- construtores;
- invariantes;
- assinaturas dos métodos;
- regras de parcelamento;
- regras de orçamento;
- regras de datas;
- arredondamento monetário.

O principal ponto pendente é definir completamente:

```python
Saida.parcelar(...)
```

e o comportamento de:

```python
Orcamento
```

---

# 29. Etapa 2 — Implementar o domínio

As primeiras classes serão implementadas em Python puro:

```text
Movimentacao
Entrada
Saida
Parcela
Conta
Categoria
Orcamento
```

Nenhuma dessas classes deverá importar Django.

---

# 30. Etapa 3 — Testar o domínio

Os testes começarão pelas regras de negócio.

Exemplos:

```text
Entrada possui impacto positivo
Saida possui impacto negativo

Saida à vista não cria parcelas

Saida parcelada gera a quantidade correta de parcelas

Valor total é distribuído corretamente

Valor da parcela gera o total correto

Soma das parcelas corresponde ao valor total

Parcelas são distribuídas pelos meses corretos

Parcela afeta o orçamento do mês correspondente

Entrada não consome orçamento

Orçamento calcula valor disponível corretamente
```

A intenção é garantir que as regras fundamentais estejam corretas antes de adicionar a complexidade do Django.

---

# 31. Etapa 4 — Persistência

Depois que o domínio estiver validado, será construída a camada de persistência.

Os Django Models representarão os dados necessários para armazenar:

```text
Conta
Categoria
Movimentacao
Parcela
Orcamento
```

A modelagem do banco será derivada das necessidades do domínio, e não o contrário.

---

# 32. Etapa 5 — Services

Somente após identificar operações que realmente coordenam múltiplos objetos serão criados services.

Um service poderá, por exemplo, coordenar:

```text
criação da saída
        ↓
parcelamento
        ↓
persistência das parcelas
        ↓
associação com conta/categoria
```

Mas não será criado um service para cada método do domínio.

---

# 33. Etapa 6 — Views

As views serão a camada de entrada HTTP.

Idealmente:

```python
def criar_saida(request):
    ...
```

deverá fazer apenas o necessário para:

1. receber os dados;
2. validar dados de interface;
3. chamar o domínio/service;
4. retornar a resposta.

As regras financeiras não devem ficar espalhadas nas views.

---

# 34. Regra de ouro da arquitetura

A arquitetura pode ser resumida pela seguinte regra:

> **O domínio decide como o negócio funciona. O Django decide como o sistema conversa com o mundo e persiste os dados.**

Ou, de forma mais operacional:

```text
Django não deve ensinar o domínio a funcionar.

O domínio deve ensinar o Django o que precisa ser persistido e exposto.
```

---

# 35. Estado atual das decisões

## Definido

- `Movimentacao` é abstrata.
- `Entrada` e `Saida` herdam de `Movimentacao`.
- `Parcela` pertence a `Saida`.
- `Parcela` não é entidade independente.
- `Conta` representa o meio/local financeiro.
- `Categoria` classifica movimentações.
- `Orcamento` representa limite por categoria/mês/ano.
- Domínio será Python puro.
- Domínio não dependerá de Django.
- Services serão usados somente quando houver coordenação entre objetos.
- Parcelas afetam o orçamento mês a mês.
- Entradas não consomem orçamento de despesas.
- A estrutura de diretórios será pequena e simples.
- O desenvolvimento começará pelo domínio e testes.

## Ainda precisa ser definido

- tipos exatos dos atributos;
- construtores;
- validações;
- assinatura definitiva de `Saida.parcelar()`;
- regra de arredondamento;
- regra para meses com dias diferentes;
- métodos definitivos de `Orcamento`;
- comportamento de `Categoria` em relação aos orçamentos;
- regras de duplicidade de orçamento;
- detalhes do mapeamento domínio ↔ Django Models.

---

# 36. Próximo passo

O próximo passo do projeto é **fechar o contrato das classes do domínio**, sem implementar Django ainda.

A sequência recomendada é:

```text
Movimentacao
   ↓
Entrada
   ↓
Saida
   ↓
Parcela
   ↓
Conta
   ↓
Categoria
   ↓
Orcamento
```

Para cada classe serão definidos:

```text
atributos
tipos
construtor
validações
métodos
retornos
exceções
invariantes
```

Depois disso, o domínio poderá ser implementado e testado isoladamente.
