### <small>Cadastro de Usuários</small>

<small>API para cadastro e busca de usuários.</small>

#### <small>Tecnologias</small>
<small>Python, FastAPI, SQLAlchemy, SQLite, Uvicorn, Pytest</small>

#### <small>Como Executar</small>

<small>Instale as dependências:</small>

```bash
pip install -r requirements.txt
```

<small>Inicie o servidor:</small>

```bash
python run.py
```

#### <small>Rotas</small>

* <small>`POST /users` — Cadastra um novo usuário.</small>
* <small>`GET /users/{user_name}` — Busca um usuário pelo nome.</small>

#### <small>Testes</small>

<small>Execute a suíte de testes com:</small>

```bash
pytest
```
