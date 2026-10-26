# 📘 Assignment: Testing FastAPI Applications

## 🎯 Objective

Escreva testes automatizados para uma API FastAPI usando `pytest` e `TestClient`. Você praticará como verificar respostas HTTP, isolar o estado entre testes e cobrir cenários de sucesso e erro.

## 📝 Tasks

### 🛠️ Configure o cliente e teste consultas

#### Descrição
Use o aplicativo de exemplo em `main.py` como sistema sob teste. Crie um arquivo `test_main.py`, configure o `TestClient` e execute os testes com `pytest`.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx`.
- Criar um cliente de testes para o aplicativo FastAPI.
- Verificar que `GET /books` responde com status `200` e retorna a lista de livros.
- Verificar que `GET /books/1` responde com status `200` e retorna o ID, título e autor esperados.

### 🛠️ Teste operações de escrita e isolamento

#### Descrição
Adicione testes para criar, atualizar e remover livros. Como o aplicativo mantém os dados em memória, prepare os dados iniciais antes de cada teste para que a ordem de execução não altere os resultados.

#### Requisitos
O programa concluído deve:

- Usar uma fixture do `pytest` para restaurar os livros iniciais antes de cada teste.
- Verificar que `POST /books` cria um livro, retorna status `201` e inclui um ID na resposta.
- Verificar que `PUT /books/{book_id}` atualiza os dados e retorna status `200`.
- Verificar que `DELETE /books/{book_id}` retorna status `204` e que o livro removido não pode mais ser consultado.

### 🛠️ Cubra validações e respostas de erro

#### Descrição
Complete a suíte com casos inválidos e IDs inexistentes. Use parametrização para testar várias entradas ou operações com a mesma estrutura de verificação.

#### Requisitos
O programa concluído deve:

- Verificar que consultar, atualizar ou remover um ID inexistente resulta em status `404`.
- Verificar que criar ou atualizar um livro sem título ou autor resulta em status `422`.
- Usar `pytest.mark.parametrize` para agrupar pelo menos dois casos de erro relacionados.
- Executar todos os testes com `python -m pytest -q` e confirmar que passam.
