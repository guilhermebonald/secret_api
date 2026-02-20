# Lock API 🔐

Uma API de gerenciamento seguro de senhas e segredos construída com **FastAPI**, **SQLAlchemy** e **criptografia robusta**.

## 📋 Sobre o Projeto

O **Lock API** é uma aplicação que permite armazenar, acessar e gerenciar senhas e dados sensíveis de forma segura. O projeto é desenvolvido em **fases progressivas**, começando com um CRUD básico e evoluindo até um sistema completo de autenticação e criptografia.

## 🚀 Fases de Desenvolvimento

### 🟢 Fase 1: Fundação (O CRUD Básico)

O objetivo desta fase é ter uma API funcional que salve e leia dados no banco de dados.

**Tarefas:**

- [x] Setup do ambiente: Criar o ambiente virtual (venv) e instalar dependências
- [x] Modelagem de Dados: Definir a tabela `Secret` (id, titulo, servico, conteudo_criptografado)
- [x] Endpoints CRUD:
  - [x] `POST /secrets` - Receber e salvar um dado
  - [x] `GET /secrets` - Listar todos
  - [x] `GET /secrets/{id}` - Buscar um específico
  - [x] `DELETE /secrets/{id}` - Deletar um registro

### 🟡 Fase 2: O Coração (Criptografia)

Garantir que, se alguém invadir o banco de dados, não consiga ler nada.

**Tarefas:**

- [ ] Implementar cryptography: Criar módulo `security.py` para lógica do Fernet
- [ ] Gerenciamento de Chaves: Salvar a chave de criptografia em arquivo `.env`
- [ ] Integração no CRUD:
  - [ ] `POST /secrets` - Criptografar o conteúdo antes de salvar
  - [ ] `GET /secrets` - Descriptografar o conteúdo na resposta
  - [ ] `GET /secrets/{id}` - Descriptografar a resposta individual

### 🔴 Fase 3: Segurança de Acesso (Auth)

Não adianta criptografar se qualquer um puder acessar os endpoints.

**Tarefas:**

- [ ] Sistema de Usuários: Criar tabela `User` com senha protegida por hashing (bcrypt/passlib)
- [ ] JWT (JSON Web Tokens): Implementar sistema de login
- [ ] Proteção de Rotas: Garantir que cada usuário veja apenas seus próprios segredos
- [ ] Endpoints de Auth:
  - [ ] `POST /auth/register` - Registrar novo usuário
  - [ ] `POST /auth/login` - Login e obtenção de token JWT
  - [ ] `POST /auth/refresh` - Renovar token expirado

### 🔵 Fase 4: Refinamento e Portfólio

O toque final para deixar o projeto com cara de profissional.

**Tarefas:**

- [ ] Documentação: Organizar nomes e descrições das rotas no Swagger (/docs)
- [ ] Tratamento de Erros: Retornar mensagens claras (ex: 404, 401, 403)
- [ ] Testes Automatizados: Criar testes com pytest
- [ ] Dockerização: Criar `Dockerfile` e `docker-compose.yml`
- [ ] CI/CD: Configurar pipelines de teste e deploy

## 🛠️ Instalação

### Pré-requisitos

- Python 3.10+
- pip ou pip3

### Setup Local

1. **Clone o repositório**

```bash
git clone <seu-repositorio>
cd lock_api
```

2. **Crie um ambiente virtual**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute a aplicação**

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📦 Dependências

- **fastapi** - Framework web moderno e rápido
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM para interação com banco de dados
- **cryptography** - Criptografia segura
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **passlib** - Hashing de senhas
- **python-jose** - Implementação de JWT
- **pydantic** - Validação de dados

## 📂 Estrutura do Projeto

```
lock_api/
├── app/
│   ├── __init__.py
│   ├── main.py           # Aplicação FastAPI e rotas
│   ├── models.py         # Modelos do SQLAlchemy
│   ├── schemas.py        # Schemas do Pydantic
│   ├── database.py       # Configuração do banco de dados
│   └── security.py       # (Fase 2) Lógica de criptografia
├── tests/                # (Fase 4) Testes automatizados
├── venv/                 # Ambiente virtual
├── .env                  # Variáveis de ambiente (não versionado)
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # (Fase 4) Configuração Docker
├── docker-compose.yml    # (Fase 4) Orquestração de containers
└── README.md             # Este arquivo

```

## 🔒 Segurança

- Senhas são criptografadas com bcrypt
- Dados sensíveis são criptografados com Fernet (AES)
- Tokens JWT para autenticação stateless
- Variáveis de ambiente para dados sensíveis

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para demonstrar conhecimentos em:
- APIs RESTful com FastAPI
- Criptografia e segurança
- Autenticação e autorização
- Boas práticas de desenvolvimento

## 📞 Contato

Se tiver dúvidas ou sugestões, entre em contato ou abra uma issue no repositório.

---

**Status**: Em desenvolvimento 🚧

Última atualização: Fevereiro de 2026
