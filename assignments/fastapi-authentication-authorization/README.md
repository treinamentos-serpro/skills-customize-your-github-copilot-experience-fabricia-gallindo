# 📘 Assignment: FastAPI Authentication and Authorization

## 🎯 Objective

Adicione autenticação com tokens Bearer e autorização por função a uma API FastAPI. Você praticará hashing de senhas, validação de tokens JWT e respostas apropriadas para acessos não autenticados ou não autorizados.

## 📝 Tasks

### 🛠️ Autenticar usuários e emitir tokens

#### Descrição
Complete o endpoint `POST /token` no código inicial. Use o formulário OAuth2 do FastAPI para receber credenciais, verificar o hash da senha e emitir um token JWT assinado com a chave `JWT_SECRET_KEY` definida no ambiente.

Instale as dependências e configure uma chave local antes de iniciar a API:

```bash
python -m pip install fastapi uvicorn PyJWT python-multipart "pwdlib[argon2]"
export JWT_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
uvicorn main:app --reload
```

As contas e senhas de demonstração do código inicial são apenas para uso local nesta atividade. Não as use em produção.

#### Requisitos
O programa concluído deve:

- Verificar senhas com `PasswordHash` sem armazenar senhas em texto puro.
- Retornar `access_token` e `token_type: "bearer"` após autenticação bem-sucedida.
- Incluir no JWT o identificador do usuário (`sub`) e uma expiração de 30 minutos.
- Responder com status `401` para usuário ou senha inválidos.

### 🛠️ Proteger endpoints com autenticação

#### Descrição
Implemente `get_current_user` para extrair e validar o token Bearer recebido pelo `OAuth2PasswordBearer`. O endpoint `GET /users/me` deve retornar os dados públicos do usuário autenticado.

#### Requisitos
O programa concluído deve:

- Validar a assinatura e a expiração do token usando somente o algoritmo `HS256`.
- Localizar a conta a partir do `sub` e rejeitar usuários inexistentes.
- Responder com status `401` e o cabeçalho `WWW-Authenticate: Bearer` se o token estiver ausente, inválido ou expirado.
- Retornar apenas nome de usuário e função em `GET /users/me`, nunca o hash da senha.

### 🛠️ Restringir acesso por função

#### Descrição
Complete a dependência `require_admin` para permitir o acesso ao endpoint `GET /admin` somente a usuários com a função `admin`. Consulte a função da conta no cadastro do servidor, em vez de confiar em uma função enviada pelo cliente.

#### Requisitos
O programa concluído deve:

- Permitir que uma conta `admin` acesse `GET /admin`.
- Responder com status `403` quando um usuário autenticado sem a função `admin` acessar `GET /admin`.
- Permitir testar login válido e inválido, token ausente e acesso de cada função em `http://127.0.0.1:8000/docs`.