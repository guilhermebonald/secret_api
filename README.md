# Lock API 🔐

Uma API de gerenciamento seguro de senhas e segredos construída com **FastAPI**, **SQLAlchemy** e **criptografia robusta**.

## ⚠️ Importante: Aviso de Segurança e Propósito Educacional

Este projeto foi desenvolvido **com propósito educacional** e para demonstrar conceitos de segurança, autenticação e criptografia em APIs.

### 🚨 Nota Crítica de Segurança

**Em um projeto de produção real**, a criptografia dos dados sensíveis **NUNCA deve ser feita no servidor (API)**. Em vez disso:

- ✅ **Abordagem Segura**: A criptografia deve ser realizada **no cliente** (frontend/aplicação do usuário)
- ✅ O cliente envia o dados **já criptografados** para o servidor
- ✅ O servidor apenas armazena e recupera dados criptografados, sem nunca acessar a chave de descriptografia
- ✅ Apenas o cliente (que possui a chave mestra) pode descriptografar os dados

**Por que?** Se o servidor criptografa e descriptografa, a chave de criptografia fica exposta no servidor. Se alguém invadir o servidor, terá acesso à chave e poderá descriptografar tudo.

### 📚 Este Projeto

Neste projeto, a criptografia é feita pelo servidor **apenas para fins educacionais**, permitindo entender como funciona a integração da criptografia em uma API. **Não use esta abordagem em produção.**

## 📋 Sobre o Projeto

O **Lock API** é uma aplicação que permite armazenar, acessar e gerenciar senhas e dados sensíveis de forma segura. O projeto é desenvolvido em **fases progressivas**, começando com um CRUD básico e evoluindo até um sistema completo de autenticação e criptografia.

## 🚀 Fases de Desenvolvimento

### 🟢 Fase 1: Fundação (O CRUD Básico) ✅ CONCLUÍDA

O objetivo desta fase é ter uma API funcional que salve e leia dados no banco de dados.

**Tarefas:**

- [x] Setup do ambiente: Criar o ambiente virtual (venv) e instalar dependências
- [x] Modelagem de Dados: Definir a tabela `Secret` (id, titulo, servico, conteudo_criptografado)
- [x] Endpoints CRUD:
  - [x] `POST /secrets` - Receber e salvar um dado
  - [x] `GET /secrets` - Listar todos
  - [x] `GET /secrets/{id}` - Buscar um específico
  - [x] `DELETE /secrets/{id}` - Deletar um registro
  - [x] `PATCH /secrets/{id}` - Atualizar um registro

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

### Endpoints Implementados

#### 🔵 Gerenciamento de Segredos

**Criar um novo segredo**
```http
POST /secrets
Content-Type: application/json

{
  "titulo": "Minha Senha",
  "servico": "GitHub",
  "conteudo": "minha_senha_secreta"
}
```

**Listar todos os segredos**
```http
GET /secrets
```

**Obter um segredo específico**
```http
GET /secrets/{secret_id}
```

**Atualizar um segredo**
```http
PATCH /secrets/{secret_id}
Content-Type: application/json

{
  "titulo": "Nova Senha",
  "servico": "GitHub",
  "conteudo": "nova_senha_secreta"
}
```

**Deletar um segredo**
```http
DELETE /secrets/{secret_id}
```

## 📦 Dependências

- **fastapi** - Framework web moderno e rápido
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM para interação com banco de dados
- **cryptography** - Criptografia segura *(próxima fase)*
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **passlib** - Hashing de senhas *(próxima fase)*
- **python-jose** - Implementação de JWT *(próxima fase)*
- **pydantic** - Validação de dados

## 📂 Estrutura do Projeto

```
lock_api/
├── app/
│   ├── __init__.py
│   ├── main.py           # ✅ Aplicação FastAPI e rotas CRUD
│   ├── models.py         # ✅ Modelos do SQLAlchemy (Secret)
│   ├── schemas.py        # ✅ Schemas do Pydantic (SecretCreate, SecretUpdate, SecretResponse)
│   ├── database.py       # ✅ Configuração do banco de dados SQLite
│   └── security.py       # 🔄 (Fase 2) Lógica de criptografia
├── tests/                # 🔄 (Fase 4) Testes automatizados
├── venv/                 # ✅ Ambiente virtual
├── .env                  # ✅ Variáveis de ambiente (não versionado)
├── .env.example          # 🔄 Exemplo de variáveis de ambiente
├── .gitignore            # ✅ Arquivos ignorados pelo Git
├── requirements.txt      # 🔄 Dependências do projeto
├── Dockerfile            # 🔄 (Fase 4) Configuração Docker
├── docker-compose.yml    # 🔄 (Fase 4) Orquestração de containers
└── README.md             # ✅ Este arquivo

🟢 ✅ Implementado | 🟡 🔄 Em Progresso | 🔴 ⏳ Não Iniciado
```

## 🔒 Segurança

### Implementação Atual (Educacional)

- Senhas são criptografadas com bcrypt
- Dados sensíveis são criptografados com Fernet (AES) **no servidor**
- Tokens JWT para autenticação stateless
- Variáveis de ambiente para dados sensíveis

### ✅ Melhorias de Segurança (Em Fases Futuras)

Para tornar este projeto mais próximo de um cenário de produção, as seguintes melhorias devem ser implementadas:

1. **Criptografia Client-Side** (Fase 2 Revisada)
   - Implementar biblioteca de criptografia no cliente
   - Dados são criptografados antes de serem enviados
   - Servidor nunca tem acesso ao texto plano

2. **End-to-End Encryption (E2EE)**
   - Cliente criptografa com sua chave privada
   - Servidor armazena apenas dados criptografados
   - Apenas o cliente consegue descriptografar

3. **Gerenciamento Seguro de Chaves**
   - Chaves armazenadas localmente no cliente
   - Nunca transmitidas ou armazenadas no servidor
   - Possibilidade de backup criptografado

4. **Zero-Knowledge Architecture**
   - Servidor não tem conhecimento dos dados armazenados
   - Servidor não pode ler, descriptografar ou recuperar dados

### 📖 Referências Educacionais

Para aprender mais sobre segurança real em aplicações de armazenamento de senhas:
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [End-to-End Encryption](https://en.wikipedia.org/wiki/End-to-end_encryption)
- [Zero-Knowledge Proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof)

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
- Criptografia e segurança (conceitos educacionais)
- Autenticação e autorização
- Boas práticas de desenvolvimento
- **Consciência sobre segurança em aplicações real-world**

## 📞 Contato

Se tiver dúvidas ou sugestões, entre em contato ou abra uma issue no repositório.

---

**Status**: Fase 1 Concluída ✅ | Fase 2 Em Progresso 🟡

Última atualização: Fevereiro de 2026
