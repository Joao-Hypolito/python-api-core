# 🎓 Sistema Acadêmico (School API & Student Management)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-LTS-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)

Projeto full-stack de **Gestão Escolar** desenvolvido durante a disciplina de **Programação para Web II** (Prof. Me. Diego H. Negretto). A aplicação é composta por uma **API RESTful** desenvolvida em Django/DRF no backend e uma **Single Page Application (SPA)** desenvolvida em Vue.js 3 no frontend.

---

## 💻 Tecnologias & Ferramentas

| Camada | Tecnologia / Lib | Descrição / Uso |
| :--- | :--- | :--- |
| **Backend** | `Python` | Linguagem principal do servidor |
| **Backend** | `Django REST Framework` | Criação de rotas, serializers, views RESTful e validação de regras de negócio |
| **Backend** | `django-cors-headers` | Liberação e controle de políticas de CORS |
| **Backend** | `SQLite` | Banco de dados relacional (desenvolvimento) |
| **Frontend** | `Vue.js 3` | Framework progressivo para construção da interface |
| **Frontend** | `Vue Router` | Gerenciamento de rotas do lado do cliente (SPA) |
| **Frontend** | `Axios` | Cliente HTTP para consumo dos endpoints da API |
| **Ambiente** | `Node.js (LTS)` | Runtime para compilação e gestão de pacotes via npm |
| **Testes** | `Postman` | Testes de integração, requisições HTTP e validações do payload JSON |

---

## 📌 Escopo do que foi Desenvolvido

### 🛠️ Backend (`school-api`)
- [x] **Gestão de Alunos (`students`)**:
  - Model `Student` com suporte a chave estrangeira (`ForeignKey`) vinculando ao curso.
  - Regra de integridade `on_delete=models.RESTRICT` para evitar exclusão acidental de cursos com alunos vinculados.
- [x] **Gestão de Professores (`teachers`)**:
  - App `teachers` desenvolvida para cadastro dos docentes (`name`, `date_of_birth` e `hire_date`).
  - Serializers e views genéricas (`Generics`) para controle completo de CRUD.
- [x] **Gestão de Cursos (`courses`) - Aula 06**:
  - App `courses` com o model `Course` (`name`, `description`).
  - Relação **Muitos-para-Muitos (NxN)** com professores usando `ManyToManyField(Teacher, related_name='courses')`.
  - Mapeamento automático de tabela intermediária no banco relacional pelo Django ORM.
  - Atualização no model `Student` estabelecendo relação **Um-para-Muitos (1xN)** com `Course`.
  - Views genéricas (`CourseCreateListView` e `CourseRetrieveUpdateDestroy`).
- [x] **Validação & Testes no Postman**:
  - Configuração de requisições HTTP (`GET`, `POST`, `PUT`, `DELETE`).
  - Envio de metadados (`Headers`), manipulação de corpos em JSON (`Body`) e testes de simulação REST.

### 🎨 Frontend (`student-management-vue`)
- [x] Inicialização do projeto Vue.js 3 utilizando suporte a **Vue Router**.
- [x] Instalação e configuração da biblioteca **Axios**.
- [x] Criação do serviço centralizador de API (`src/services/api.js`) com métodos de CRUD.
- [x] Criação da página `HomeView.vue` com tela de recepção do sistema.
- [x] Criação da página `StudentView.vue` integrando formulários interativos, tratamento de datas e tabela de gerenciamento de alunos.
- [x] Configuração do middleware `CORS` no Django para permitir requisições da porta local `:5173` do Vite/Vue.

---

## 🌐 Endpoints da API

### 👨‍🎓 Alunos (`/students/`)
| Método | Endpoint | Função / Descrição | Status HTTP |
| :---: | :--- | :--- | :---: |
| `GET` | `/students/` | Lista todos os alunos cadastrados | `200 OK` |
| `POST` | `/students/` | Cadastra um novo aluno no banco de dados (exige `course_id`) | `201 Created` |
| `GET` | `/students/<id>` | Retorna os detalhes de um aluno específico | `200 OK` |
| `PUT` | `/students/<id>` | Atualiza todos os dados do aluno por ID | `200 OK` |
| `DELETE` | `/students/<id>` | Remove o registro do aluno do sistema | `204 No Content` |

### 👨‍🏫 Professores (`/teachers/`)
| Método | Endpoint | Função / Descrição | Status HTTP |
| :---: | :--- | :--- | :---: |
| `GET` | `/teachers/` | Lista todos os professores cadastrados | `200 OK` |
| `POST` | `/teachers/` | Cadastra um novo professor | `201 Created` |
| `GET` | `/teachers/<id>` | Retorna os detalhes de um professor específico | `200 OK` |
| `PUT` | `/teachers/<id>` | Atualiza todos os dados do professor | `200 OK` |
| `DELETE` | `/teachers/<id>` | Remove o registro do professor | `204 No Content` |

### 📚 Cursos (`/courses/`)
| Método | Endpoint | Função / Descrição | Status HTTP |
| :---: | :--- | :--- | :---: |
| `GET` | `/courses/` | Lista todos os cursos cadastrados | `200 OK` |
| `POST` | `/courses/` | Cadastra um novo curso e associa professores (`teachers: [ids]`) | `201 Created` |
| `GET` | `/courses/<id>` | Retorna os detalhes de um curso específico | `200 OK` |
| `PUT` | `/courses/<id>` | Atualiza dados do curso e lista de professores | `200 OK` |
| `DELETE` | `/courses/<id>` | Apaga o curso (bloqueado se houver alunos matriculados - `RESTRICT`) | `204 No Content` / `400 Bad Request` |

---

## 🔗 Regras de Negócio & Relacionamentos

1. **Curso x Professor (NxN - ManyToMany)**: Um curso pode ser ministrado por vários professores, e um professor pode ministrar aulas em vários cursos.
2. **Aluno x Curso (1xN - ForeignKey)**: Um aluno só pode estar matriculado em um curso por vez. Um curso, porém, possui múltiplos alunos.
3. **Integridade Referencial (`models.RESTRICT`)**: Impede a exclusão acidental de cursos que possuem alunos ativos matriculados, evitando registros órfãos no banco de dados.

---

## 📂 Estrutura das Pastas

```text
.
├── school-api/                    # Projeto Backend (Django REST Framework)
│   ├── app/                       # Configurações globais do projeto (settings.py, urls.py)
│   ├── students/                  # App de Gestão de Alunos (Models, Views, Serializers)
│   ├── teachers/                  # App de Gestão de Professores (Models, Views, Serializers)
│   ├── courses/                   # App de Gestão de Cursos (Models, Views, Serializers, NxN)
│   └── manage.py
│
└── student-management-vue/        # Projeto Frontend (Vue.js 3)
    ├── src/
    │   ├── services/
    │   │   └── api.js             # Instância do Axios (BaseURL: http://localhost:8000)
    │   ├── router/
    │   │   └── index.js           # Mapeamento de rotas SPA
    │   ├── views/
    │   │   ├── HomeView.vue       # Tela inicial
    │   │   └── StudentView.vue    # Tela de CRUD de Alunos
    │   ├── App.vue                # Componente Raiz
    │   └── main.js
    └── package.json