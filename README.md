# Secret API 🔐

Uma API de gerenciamento seguro de senhas e segredos construída com **FastAPI**, **SQLAlchemy** e **Fernet (AES-128)**.

## ⚠️ Aviso Importante

**Propósito Educacional**: Este projeto criptografa dados no servidor para fins de aprendizado.

**Em produção real**: A criptografia deve ser feita no **cliente**, não no servidor. Assim o servidor nunca tem acesso às chaves ou dados descriptografados. [Saiba mais sobre E2EE](https://en.wikipedia.org/wiki/End-to-end_encryption)

## 🚀 Fases de Desenvolvimento

- ✅ **Fase 1**: CRUD básico (Concluído)
- ✅ **Fase 2**: Criptografia com Fernet (Concluído)
- ⏳ **Fase 3**: Autenticação JWT (Planejado)
- ⏳ **Fase 4**: Docker & Testes (Planejado)

## 🛠️ Instalação Rápida

```bash
# Clone e acesse o projeto
git clone <seu-repositorio>
cd lock_api

# Crie ambiente virtual e instale dependências
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou no Windows: venv\Scripts\activate

pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env
# Adicione SECRET_KEY gerada pelo Fernet

# Execute
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs (Swagger) ou http://localhost:8000/redoc

## 📚 Endpoints Disponíveis

| Método | Rota            | Descrição                        |
| ------ | --------------- | -------------------------------- |
| POST   | `/secrets`      | Criar novo segredo (criptografa) |
| GET    | `/secrets`      | Listar todos os segredos         |
| GET    | `/secrets/{id}` | Obter segredo (descriptografa)   |
| PATCH  | `/secrets/{id}` | Atualizar segredo (criptografa)  |
| DELETE | `/secrets/{id}` | Deletar um segredo               |

### Exemplo de Uso

```bash
# 1. Criar segredo (conteúdo será criptografado automaticamente)
curl -X POST "http://localhost:8000/secrets" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"GitHub","servico":"git","conteudo":"token123"}'

# Resposta: ID será 1

# 2. Listar todos (conteúdo permanece CRIPTOGRAFADO no banco)
curl "http://localhost:8000/secrets"

# 3. Obter específico (conteúdo é DESCRIPTOGRAFADO automaticamente)
curl "http://localhost:8000/secrets/1"

# 4. Atualizar conteúdo (será criptografado automaticamente) ✅
curl -X PATCH "http://localhost:8000/secrets/1" \
  -H "Content-Type: application/json" \
  -d '{"conteudo":"novo_token456"}'

# 5. Atualizar apenas título (sem mexer no conteúdo)
curl -X PATCH "http://localhost:8000/secrets/1" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"GitHub Pessoal"}'

# 6. Deletar
curl -X DELETE "http://localhost:8000/secrets/1"
```

## 📦 Dependências Principais

- **fastapi** - Framework web assíncrono
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM para banco de dados
- **pydantic** - Validação de dados
- **cryptography** - Criptografia com Fernet
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📂 Estrutura

```
lock_api/
├── app/
│   ├── main.py          # Endpoints da API (POST, GET, PATCH, DELETE)
│   ├── models.py        # Modelo Secret com conteudo_criptografado
│   ├── schemas.py       # Schemas Pydantic (SecretCreate, SecretUpdate, SecretResponse)
│   ├── database.py      # Configuração SQLite
│   ├── security.py      # Funções encrypt_data() e decrypt_data()
│   └── __init__.py
├── .qodo/               # Configurações Qodo (IA)
├── venv/                # Ambiente virtual
├── .env                 # Variáveis de ambiente (não commitar)
├── .gitignore           # Arquivos ignorados
├── README.md            # Este arquivo
└── requirements.txt     # Dependências Python
```

## 🔒 Segurança - Fase 2 ✅ Concluída

### ✅ Implementado

- ✅ **Criptografia Fernet (AES-128)** em [app/security.py](app/security.py)
  - `encrypt_data(conteudo: str)` → conteúdo criptografado
  - `decrypt_data(conteudo_criptografado: str)` → conteúdo original

- ✅ **Dados SEMPRE criptografados no banco**
  - Campo `conteudo_criptografado` em [app/models.py](app/models.py)
  - Formato: `gAAAAABa3X7wDX...` (base64)

- ✅ **Criptografia automática no POST**
  - POST `/secrets` criptografa automaticamente

- ✅ **Descriptografia automática no GET**
  - GET `/secrets/{id}` descriptografa antes de retornar
  - GET `/secrets` retorna conteúdo criptografado

- ✅ **Update com criptografia**
  - PATCH `/secrets/{id}` criptografa novo conteúdo automaticamente
  - Suporta atualizações parciais (título, serviço ou conteúdo)

- ✅ **Variáveis de ambiente**
  - `SECRET_KEY` carregada do `.env`
  - Gerenciada por `python-dotenv`

### ⏳ Próximas Melhorias

- ⏳ **CORS e validação avançada**
- ⏳ **Autenticação JWT** (Fase 3)
- ⏳ **Rate limiting e proteção contra ataques**
- ⏳ **Testes unitários**
- ⏳ **Docker & CI/CD**

## 🔧 Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_fernet_aqui
```

**Para gerar uma chave Fernet:**

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())  # Copie este valor para SECRET_KEY no .env
```

## 🧪 Teste Completo do Update

```bash
# 1. Criar
curl -X POST "http://localhost:8000/secrets" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"GitHub","servico":"git","conteudo":"token_antigo"}'

# 2. Listar (vê conteúdo CRIPTOGRAFADO)
curl "http://localhost:8000/secrets" | jq '.[] | {titulo, conteudo_criptografado}'

# Saída: "conteudo_criptografado": "gAAAAABa3X7wDX..."

# 3. Atualizar conteúdo
curl -X PATCH "http://localhost:8000/secrets/1" \
  -H "Content-Type: application/json" \
  -d '{"conteudo":"token_novo_secreto"}'

# 4. Verificar no banco (deve estar DIFERENTE e CRIPTOGRAFADO)
curl "http://localhost:8000/secrets" | jq '.[] | {titulo, conteudo_criptografado}'

# Saída: "conteudo_criptografado": "gAAAAABx9K4aZY..." (mudou!)

# 5. Descriptografar ao buscar
curl "http://localhost:8000/secrets/1" | jq '.conteudo'

# Saída: "token_novo_secreto" ✅
```

## 📖 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Cryptography.io - Fernet](https://cryptography.io/en/latest/fernet/)
- [OWASP Security](https://owasp.org/)
- [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

## 📝 Licença

MIT - Veja LICENSE para detalhes

---

**Status**: Fase 1 ✅ | Fase 2 ✅ | Fase 3 ⏳

Última atualização: 24 de Fevereiro de 2026
