# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI e modelos Pydantic. Você praticará endpoints HTTP, operações CRUD, validação de dados e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar endpoints para consultar livros

#### Descrição
Use o código inicial em `main.py` para implementar endpoints que listem os livros cadastrados e consultem um livro pelo ID. No terminal, dentro da pasta desta atividade, instale as dependências e inicie o servidor:

```bash
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` para explorar e testar a API pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Retornar todos os livros ao receber `GET /books`.
- Retornar um livro específico ao receber `GET /books/{book_id}`.
- Responder com status `404` quando o ID consultado não existir.

### 🛠️ Implementar operações de criação, atualização e remoção

#### Descrição
Complete os endpoints para adicionar um livro, atualizar os dados de um livro existente e removê-lo. Mantenha os dados em memória; não é necessário usar um banco de dados.

#### Requisitos
O programa concluído deve:

- Criar um livro com `POST /books`, gerar um ID único e responder com status `201`.
- Atualizar título e autor com `PUT /books/{book_id}` e responder com status `200`.
- Remover um livro com `DELETE /books/{book_id}` e responder com status `204`.
- Responder com status `404` ao tentar atualizar ou remover um ID inexistente.

### 🛠️ Validar dados e testar a API

#### Descrição
Use os modelos Pydantic para validar os dados recebidos e teste os fluxos de sucesso e de erro pela documentação interativa em `/docs`.

#### Requisitos
O programa concluído deve:

- Exigir título e autor com pelo menos um caractere, usando `Field(min_length=1)`.
- Rejeitar dados inválidos com a resposta de validação padrão do FastAPI (`422`).
- Permitir testar a sequência de criar, consultar, atualizar e remover um livro.