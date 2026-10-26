# 📘 Assignment: FastAPI and SQLite Persistence

## 🎯 Objective

Atualize uma API de livros feita com FastAPI para persistir os dados em SQLite. Você praticará consultas SQL parametrizadas e operações CRUD que continuam disponíveis após reiniciar o servidor.

## 📝 Tasks

### 🛠️ Consultar livros armazenados no SQLite

#### Descrição
Use o código inicial em `main.py`, que prepara o banco `books.db` e cria a tabela `books`. Implemente os endpoints de consulta usando conexões SQLite e instruções `SELECT`.

Para executar a API, instale as dependências e inicie o servidor a partir desta pasta:

```bash
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

Use `http://127.0.0.1:8000/docs` para testar os endpoints.

#### Requisitos
O programa concluído deve:

- Retornar todos os livros com `GET /books`.
- Retornar um livro pelo ID com `GET /books/{book_id}`.
- Responder com status `404` quando o livro consultado não existir.

### 🛠️ Persistir operações CRUD

#### Descrição
Implemente a criação, atualização e remoção de livros usando as instruções `INSERT`, `UPDATE` e `DELETE` do SQLite. Use os códigos de status HTTP definidos no código inicial.

#### Requisitos
O programa concluído deve:

- Criar livros com `POST /books`, retornando o livro criado com status `201`.
- Atualizar título e autor com `PUT /books/{book_id}`, retornando status `200`.
- Remover livros com `DELETE /books/{book_id}`, retornando status `204`.
- Responder com status `404` quando a atualização ou remoção usar um ID inexistente.
- Usar parâmetros SQL (`?`) para passar valores às consultas, sem concatenar dados recebidos na instrução SQL.

### 🛠️ Verificar a persistência dos dados

#### Descrição
Teste o fluxo completo pela documentação interativa. Crie um livro, reinicie o servidor e consulte o mesmo ID para confirmar que os dados foram gravados no arquivo SQLite.

#### Requisitos
O programa concluído deve:

- Manter os livros criados ou atualizados após o encerramento e a reinicialização do servidor.
- Permitir concluir a sequência de criar, consultar, atualizar, consultar novamente e remover um livro.
- Continuar retornando `404` ao consultar um ID após ele ser removido.