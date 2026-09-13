# 🎓 Sistema Acadêmico (School API & Student Management)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://aistudio.google.com/)
[![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
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
| **Backend** | `google-genai` | SDK Oficial do Google para integração com o modelo de IA **Gemini 2.5 Flash** |
| **Backend** | `python-dotenv` | Gestão de variáveis de ambiente sigilosas (`.env`) como chaves de API |
| **Backend** | `django-cors-headers` | Liberação e controle de políticas de CORS |
| **Backend** | `MySQL` | Banco de dados relacional (produção/desenvolvimento) |
| **Backend** | `mysqlclient` / `PyMySQL` | Driver de conexão do Python com o MySQL |
| **Frontend** | `Vue.js 3` | Framework progressivo para construção da interface |
| **Frontend** | `Vue Router` | Gerenciamento de rotas do lado do cliente (SPA) |
| **Frontend** | `Axios` | Cliente HTTP para consumo dos endpoints da API |
| **Ambiente** | `Node.js (LTS)` | Runtime para compilação e gestão de pacotes via npm |
| **Testes** | `Postman` | Testes de integração, requisições HTTP e validações do payload JSON |

---

## 📌 Escopo do que foi Desenvolvido

### 🛠️ Backend (`school-api`)

- [x] **Integração com Google Gemini API - Aula 11**:
  - Desenvolvimento do módulo independente `gemini_api/client.py` e configuração da autenticação utilizando o SDK `google-genai`.
  - Definição do modelo `gemini-2.5-flash` para geração automatizada de resumos e descrições acadêmicas com limite de 250 caracteres.
  - Proteção da chave de API (`API_KEY`) por meio de arquivo `.env` e da biblioteca `python-dotenv`.

- [x] **Automação utilizando Django Signals (`pre_save`)**:
  - Criação do arquivo `signals.py` no app `courses`, responsável por monitorar o evento `pre_save` do modelo `Course`.
  - Geração automática do campo `description` utilizando Inteligência Artificial durante a criação de um curso quando nenhuma descrição é fornecida.
  - Registro e ativação do listener de sinais através do método `ready()` em `apps.py` (`CoursesConfig`).

- [x] **Configuração do Banco de Dados MySQL - Aula 09**:
  - Implementação da persistência de dados utilizando o SGBD relacional **MySQL**.
  - Configuração da `School-API` para conexão com o banco através da engine `django.db.backends.mysql`.
  - Aplicação das migrations responsáveis pela criação das tabelas relacionais (`students`, `teachers`, `courses`).

- [x] **Gerenciamento de Alunos (`students`)**:
  - Implementação do model `Student` com utilização de chave estrangeira (`ForeignKey`) para associação com o curso.
  - Aplicação da regra de integridade `on_delete=models.RESTRICT`, impedindo a remoção de cursos que possuam alunos associados.

- [x] **Gerenciamento de Professores (`teachers`)**:
  - Desenvolvimento do app `teachers` para gerenciamento dos dados dos professores (`name`, `date_of_birth` e `hire_date`).
  - Implementação de Serializers e views genéricas (`Generics`) para disponibilizar as operações completas de CRUD.

- [x] **Gerenciamento de Cursos (`courses`)**:
  - Desenvolvimento do app `courses` contendo o model `Course` (`name`, `description`).
  - Implementação de relacionamento **Muitos-para-Muitos (NxN)** entre cursos e professores utilizando `ManyToManyField(Teacher, related_name='courses')`.
  - Utilização do Django ORM para gerenciamento automático da tabela intermediária no banco de dados relacional.
  - Atualização do model `Student` para estabelecer o relacionamento **Um-para-Muitos (1xN)** com `Course`.
  - Implementação das views genéricas `CourseCreateListView` e `CourseRetrieveUpdateDestroy`.

- [x] **Validação e Testes utilizando Postman**:
  - Configuração e execução de requisições HTTP (`GET`, `POST`, `PUT`, `DELETE`).
  - Configuração de metadados por meio de `Headers` e envio de dados estruturados no formato JSON através do `Body`.
  - Realização de testes das operações da API seguindo o padrão REST.

### 🎨 Frontend (`student-management-vue`)
- [x] Inicialização do projeto Vue.js 3 utilizando suporte a **Vue Router**.
- [x] Instalação e configuração da biblioteca **Axios**.
- [x] Criação do serviço centralizador de API (`src/services/api.js`) com métodos de CRUD.
- [x] Criação da página `HomeView.vue` com tela de recepção do sistema.
- [x] Criação da página `StudentView.vue` integrando formulários interativos, tratamento de datas e tabela de gerenciamento de alunos.
- [x] Configuração do middleware `CORS` no Django para permitir requisições da porta local `:5173` do Vite/Vue.

---

## 🔑 Variáveis de Ambiente & Configuração da IA

Para habilitar a geração automática de descrições dos cursos com o Google Gemini, crie um arquivo chamado `.env` na raiz do projeto Django (`school-api/`) contendo sua chave da API:

```env
API_KEY="SuaChaveDoGoogleAiStudio"