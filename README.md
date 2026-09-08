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
  - Criação do módulo desacoplado `gemini_api/client.py` e configuração de autenticação via SDK `google-genai`.
  - Configuração do modelo `gemini-2.5-flash` para geração automática de resumos e descrições acadêmicas limitadas a 250 caracteres.
  - Armazenamento seguro da chave de API (`API_KEY`) utilizando arquivo `.env` e a biblioteca `python-dotenv`.
- [x] **Automação via Django Signals (`pre_save`)**:
  - Implementação do arquivo `signals.py` no app `courses` escutando o evento `pre_save` do modelo `Course`.
  - Preenchimento automático do campo `description` via Inteligência Artificial no momento da criação do curso caso o campo seja enviado em branco.
  - Registro e inicialização do listener de sinal no método `ready()` do `apps.py` (`CoursesConfig`).
- [x] **Migração de Banco de Dados (MySQL) - Aula 09**:
  - Integração e persistência de dados em um SGBD relacional **MySQL**.
  - Configuração da `School-API` para comunicação remota/local via engine `django.db.backends.mysql`.
  - Execução de migrations para criação das tabelas relacionais (`students`, `teachers`, `courses`).
- [x] **Gestão de Alunos (`students`)**:
  - Model `Student` com suporte a chave estrangeira (`ForeignKey`) vinculando ao curso.
  - Regra de integridade `on_delete=models.RESTRICT` para evitar exclusão acidental de cursos com alunos vinculados.
- [x] **Gestão de Professores (`teachers`)**:
  - App `teachers` desenvolvida para cadastro dos docentes (`name`, `date_of_birth` e `hire_date`).
  - Serializers e views genéricas (`Generics`) para controle completo de CRUD.
- [x] **Gestão de Cursos (`courses`)**:
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

## 🔑 Variáveis de Ambiente & Configuração da IA

Para habilitar a geração automática de descrições dos cursos com o Google Gemini, crie um arquivo chamado `.env` na raiz do projeto Django (`school-api/`) contendo sua chave da API:

```env
API_KEY="SuaChaveDoGoogleAiStudio"