# 🎓 Sistema Acadêmico (School API & Student Management)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-LTS-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)

Projeto full-stack de **Gestão Escolar** desenvolvido durante as **Aulas 04 e 05** da disciplina de **Programação para Web II**. A aplicação é composta por uma **API RESTful** desenvolvida em Django/DRF no backend e uma **Single Page Application (SPA)** desenvolvida em Vue.js 3 no frontend.

---

## 💻 Tecnologias & Ferramentas

| Camada | Tecnologia / Lib | Descrição / Uso |
| :--- | :--- | :--- |
| **Backend** | `Python` | Linguagem principal do servidor |
| **Backend** | `Django REST Framework` | Criação das rotas, serializers e views RESTful |
| **Backend** | `django-cors-headers` | Liberação e controle de políticas de CORS |
| **Backend** | `SQLite` | Banco de dados relacional (desenvolvimento) |
| **Frontend** | `Vue.js 3` | Framework progressivo para construção da interface |
| **Frontend** | `Vue Router` | Gerenciamento de rotas do lado do cliente (SPA) |
| **Frontend** | `Axios` | Cliente HTTP para consumo dos endpoints da API |
| **Ambiente** | `Node.js (LTS)` | Runtime para compilação e gestão de pacotes via npm |

---

## 📌 Escopo do que foi Desenvolvido

### 🛠️ Backend (`school-api`) — Aula 04
- [x] Configuração inicial do projeto Django e ambiente virtual (`venv`).
- [x] Instalação do **Django REST Framework**.
- [x] Criação da app `students` e do modelo `Student` (`name` e `date_of_birth`).
- [x] Implementação do `StudentSerializer` para conversão dos modelos em JSON.
- [x] Criação das views genéricas `StudentCreateListView` e `StudentRetrieveUpdateDestroyView`.
- [x] Mapeamento dos endpoints RESTful em `urls.py`.
- [x] **Desafio / Atividade:** Construção da app `teachers` (`name`, `date_of_birth` e `hire_date`).

### 🎨 Frontend (`student-management-vue`) — Aula 05
- [x] Inicialização do projeto Vue.js 3 utilizando suporte a **Vue Router**.
- [x] Instalação e configuração da biblioteca **Axios**.
- [x] Criação do serviço centralizador de API (`src/services/api.js`) com métodos de CRUD.
- [x] Criação da página `HomeView.vue` com tela de recepção do sistema.
- [x] Criação da página `StudentView.vue` integrando formulários interativos, tratamento de datas e tabela de gerenciamento de alunos.
- [x] Configuração do middleware `CORS` no Django para permitir requisições da porta local `:5173` do Vite/Vue.

---

## 🌐 Endpoints da API

| Método | Endpoint | Função / Descrição | Status HTTP |
| :---: | :--- | :--- | :---: |
| `GET` | `/students/` | Lista todos os alunos cadastrados[cite: 2] | `200 OK` |
| `POST` | `/students/` | Cadastra um novo aluno no banco de dados[cite: 2] | `201 Created` |
| `GET` | `/students/<id>` | Retorna os detalhes de um aluno específico[cite: 2] | `200 OK` |
| `PUT` | `/students/<id>` | Atualiza todos os dados do aluno por ID[cite: 2] | `200 OK` |
| `DELETE` | `/students/<id>` | Remove o registro do aluno do sistema[cite: 2] | `204 No Content` |

---

## 📂 Estrutura das Pastas

```text
.
├── school-api/                    # Projeto Backend (Django)
│   ├── app/                       # Configurações globais do projeto
│   │   ├── settings.py            # Configuração de APPS, CORS e Middleware
│   │   └── urls.py                # Rotas principais da API
│   ├── students/                  # App de Gestão de Alunos
│   │   ├── models.py              # Entidade Student
│   │   ├── serializers.py         # Conversão Model -> JSON
│   │   └── views.py               # Lógica do CRUD (Generics)
│   └── manage.py
│
└── student-management-vue/        # Projeto Frontend (Vue.js)
    ├── src/
    │   ├── services/
    │   │   └── api.js             # Instância do Axios (BaseURL: 8000)
    │   ├── router/
    │   │   └── index.js           # Mapeamento de rotas SPA
    │   ├── views/
    │   │   ├── HomeView.vue       # Tela inicial
    │   │   └── StudentView.vue    # Tela de CRUD de Alunos
    │   ├── App.vue                # Componente Raiz
    │   └── main.js
    └── package.json