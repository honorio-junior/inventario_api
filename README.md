# Inventário API

Uma API para gerenciar categorias, estoques e produtos em python, usando FastAPI e SQLite3.

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido para construir APIs com Python 3.7+.
- **SQLite3**: Um banco de dados leve e embutido para armazenar dados.

## Funcionalidades

- Listar categorias
- Listar estoques
- Listar produtos de um estoque específico
- Criar categorias de produtos
- Criar estoques de produtos
- Criar produtos em um estoque específico
- Apagar estoque
- Apagar produtos de um estoque específico
- Apagar categoria
- ~~Atualizar produto~~
- ~~Atualizar categoria~~

## Iniciando a API

1. Clone o repositório:

   ```bash
   git clone https://github.com/honorio-junior/inventario_api.git
   cd inventario_api
   ```
2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
    ```
3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```
4. Configuração do banco de dados:

    ```bash
    python .\api\database.py
    ```
5. Executando a API:

    ```bash
    fastapi dev .\api\run.py
    ```
**A API estará disponível em** http://127.0.0.1:8000

**A Documentação em** http://127.0.0.1:8000/docs

## Iniciando a API com Docker
```bash
git clone https://github.com/honorio-junior/inventario_api.git
cd inventario_api
docker compose up
```
**A API estará disponível em** http://127.0.0.1:8000

**A Documentação em** http://127.0.0.1:8000/docs
