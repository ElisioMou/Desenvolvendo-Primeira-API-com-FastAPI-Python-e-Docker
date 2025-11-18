# Desenvolvendo-Primeira-API-com-FastAPI-Python-e-Docker


## Desafio de projeto 5 - Santander 2025 Back-End com Python

### 🚀 Objetivo:

Desenvolver uma API utilizando **FastAPI**, **Python**, **SQLAlchemy** e **MySQL**, seguindo as boas práticas de arquitetura, organização modular, tipagem e tratamento de exceções. O projeto deve incluir:
* CRUD completo de *Atletas*
* Filtros via **Query Parameters** (nome, CPF)
* Customização de responses
* Manipulação de exceções
* Integração com banco MySQL usando SQLAlchemy ORM
##

### 📁 Estrutura do Projeto:

```
WORKOUT_API/
│-- app/
│   │-- api/
│   │   └── v1/
│   │       ├── routers/
│   │       └── schemas/
│   │-- core/
│   │-- models/
│   │-- repositories/
│   │-- services/
│   └── main.py
│
├── requirements.txt
└── README.md
```
### 🛠️ Tecnologias utilizadas:

* **Python 3.10+**
* **FastAPI**
* **SQLAlchemy ORM**
* **MySQL 8+**
* **Uvicorn** (server ASGI)
  
##

## ⚙️ Configuração do Ambiente

### 1️⃣ Criação do ambiente virtual

```sh
python -m venv venv
venv\Scripts\activate      # Windows
```
<img src="https://github.com/user-attachments/assets/6c19eb65-cace-4f99-ad1e-8d0f27dfac03">

### 2️⃣ Instalação de dependências

```sh
pip install -r requirements.txt
```

### 3️⃣ Subir a aplicação

```sh
uvicorn app.main:app --reload
```

API disponível em:

```
http://127.0.0.1:8000
```
<img src="https://github.com/user-attachments/assets/505457c9-79d4-4178-9ef2-71814695792a">


## 🗄️ Banco de Dados do MySQL🐬

Criação do banco através do arquivo `.env`:

```
DB_USER=root
DB_PASSWORD=senha
DB_HOST=db
DB_PORT=3306
DB_NAME=workout_db
```

A aplicação cria tabelas automaticamente usando SQLAlchemy.

<img src="https://github.com/user-attachments/assets/e5ed4a1b-02ac-43ed-ab6c-52315d2a67ab">

---

## 🧩 Endpoints Principais

### 🔹 GET /atletas

Retorna todos os atletas com os campos:

* nome
* centro_treinamento
* categoria


### 🔹 POST /atletas

Cria um novo atleta.

### Body (JSON)

```json
{
  "nome": "Carlos Silva",
  "cpf": "12345678910",
  "idade": 25,
  "centro_treinamento": "CT Leste",
  "categoria": "Avançado"
}
```


### 🔹 PUT /atletas/{id}

Atualiza um atleta específico.

### 🔹 DELETE /atletas/{id}

Remove um atleta.
<br> 

---

## ‼️Tratamento de Exceções

O projeto implementa exceptions personalizadas, como:

* Atleta não encontrado
* CPF já cadastrado
* Erros de validação
Todas retornam respostas JSON amigáveis.

---
<br>

## 🐳 Docker (opcional)

### Docker, após configurar `docker-compose.yml`:

```sh
docker-compose up --build -d
```

### 🔹A API rodará em container:
<img src="https://github.com/user-attachments/assets/1cfb97fd-7dc9-4091-b838-cd26ccd68f86">

### 🔹⚗️ Docker Compose e configuração do Alembic:
<img src="https://github.com/user-attachments/assets/e151fab0-3a8c-496f-9125-0d6b9af88180">

---
<br>

## ♻️ Migrations + Criação das rotas e configuração dos endpoints

### 🔹Execução docker-compose uploading:
<img src="https://github.com/user-attachments/assets/0b4e55ff-f98f-4786-ab4f-3a9f2a625631">

### 🔹Endpoints via Swagger UI:
<img src="https://github.com/user-attachments/assets/b81f02d1-d048-492d-a7fe-728c98d48ab6">

##

<img src="https://github.com/user-attachments/assets/1a5dff61-9071-4a1b-8e33-b5d9e12c21ea">

---

# ✨ Autor

Projeto desenvolvido por **Elisio Moura**, como parte de estudos avançados em FastAPI, boas práticas de backend e arquitetura limpa.

Sinta-se livre para contribuir, abrir issues ou sugerir melhorias!
