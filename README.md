# Nexo

Projeto Django para gestão de movimentações financeiras e orçamentos mensais.

## Visão geral

Este aplicativo auxilia no controle de:

- entradas e saídas financeiras;
- parcelas e movimentações;
- limites e metas de orçamento;
- listagem e cadastro de registros via interface web.

## Tecnologias

- Python
- Django
- PostgreSQL
- Pytest

## Requisitos

- Python 3.10+
- pip
- PostgreSQL em execução

## Configuração do banco de dados

O projeto utiliza PostgreSQL via `dj_database_url` e lê a URL de conexão a partir da variável de ambiente `POSTGRES_DB_URL`.

Crie um arquivo `.env` na raiz do projeto com algo como:

```env
POSTGRES_DB_URL=postgres://usuario:senha@localhost:5432/nexo
```

Se preferir, pode usar uma URL PostgreSQL em formato completo, por exemplo:

```env
POSTGRES_DB_URL=postgresql://postgres:postgres@localhost:5432/nexo
```

## Como executar

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Verifique se o PostgreSQL está acessível e o banco existe.

4. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor local:

   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:

   ```text
   http://127.0.0.1:8000/
   ```

## Testes

Para executar os testes do projeto:

```bash
pytest
```

## Estrutura principal

- `nexo/` — aplicação principal do projeto
- `nexo_config/` — configuração do Django
- `tests/` — testes automatizados
- `manage.py` — entrypoint do projeto

## Observações

Este README é um ponto de partida. Ajustes podem ser feitos conforme a aplicação evolui e novos módulos forem adicionados.
