# Lock API 🔐

Uma API de gerenciamento seguro de senhas e segredos construída com **FastAPI**, **SQLAlchemy** e **criptografia**.

## ⚠️ Aviso Importante

**Propósito Educacional**: Este projeto criptografa dados no servidor para fins de aprendizado.

**Em produção real**: A criptografia deve ser feita no **cliente**, não no servidor. Assim o servidor nunca tem acesso às chaves ou dados descriptografados. [Saiba mais sobre E2EE](https://en.wikipedia.org/wiki/End-to-end_encryption)

## 🚀 Fases de Desenvolvimento

- ✅ **Fase 1**: CRUD básico (Concluído)
- 🟡 **Fase 2**: Criptografia real (Em progresso)
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
pip install -r requirements.txt

# Execute
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs (Swagger) ou http://localhost:8000/redoc

## � Endpoints Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/secrets` | Criar novo segredo |
| GET | `/secrets` | Listar todos os segredos |
| GET | `/secrets/{id}` | Obter um segredo |
| PATCH | `/secrets/{id}` | Atualizar um segredo |
| DELETE | `/secrets/{id}` | Deletar um segredo |

### Exemplo de Uso

```bash
# Criar
curl -X POST "http://localhost:8000/secrets" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"GitHub","servico":"git","conteudo":"token123"}'

# Listar
curl "http://localhost:8000/secrets"
```

## � Dependências Principais

- **fastapi** - Framework web
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM para banco de dados
- **pydantic** - Validação de dados
## 📂 Estrutura

```
lock_api/
├── app/
│   ├── main.py          # API e endpoints
│   ├── models.py        # Modelos SQL
│   ├── schemas.py       # Schemas Pydantic
│   ├── database.py      # Configuração BD
│   └── security.py      # Criptografia (próximo)
├── venv/                # Ambiente virtual
├── .env                 # Variáveis de ambiente
├── .gitignore           # Git ignore
└── README.md            # Este arquivo
```

## 🔒 Segurança

- Dados sensíveis armazenados no banco (implementação futura)
- Variáveis de ambiente para chaves
- CORS e validação de entrada (a implementar)
- Autenticação JWT (próxima fase)

## 📖 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OWASP Security](https://owasp.org/)
- [Cryptography Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

## 📝 Licença

MIT - Veja LICENSE para detalhes

---

**Status**: Fase 1 ✅ | Fase 2 🟡

Última atualização: Fevereiro de 2026