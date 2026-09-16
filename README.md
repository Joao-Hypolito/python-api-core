# 🎓 Sistema Acadêmico (School API & Student Management)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://aistudio.google.com/)
[![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-LTS-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)

Full-stack **School Management** project developed during the **Web Programming II** course (Prof. M.Sc. Diego H. Negretto). The application consists of a **RESTful API** built with Django/DRF on the backend and a **Single Page Application (SPA)** built with Vue.js 3 on the frontend.

---

## 💻 Technologies & Tools

| Layer | Technology / Lib | Description / Usage |
| :--- | :--- | :--- |
| **Backend** | `Python` | Main server language |
| **Backend** | `Django REST Framework` | Route creation, serializers, RESTful views, and business rule validation |
| **Backend** | `google-genai` | Official Google SDK for integration with the **Gemini 2.5 Flash** AI model |
| **Backend** | `python-dotenv` | Management of sensitive environment variables (`.env`) such as API keys |
| **Backend** | `django-cors-headers` | Management and enabling of CORS policies |
| **Backend** | `MySQL` | Relational database (production/development) |
| **Backend** | `mysqlclient` / `PyMySQL` | Python driver for MySQL connection |
| **Frontend** | `Vue.js 3` | Progressive framework for building the user interface |
| **Frontend** | `Vue Router` | Client-side route management (SPA) |
| **Frontend** | `Axios` | HTTP client for consuming API endpoints |
| **Environment** | `Node.js (LTS)` | Runtime for compilation and package management via npm |
| **Testing** | `Postman` | Integration testing, HTTP requests, and JSON payload validation |

---

## 📌 Scope of What Was Developed

### 🛠️ Backend (`school-api`)

- [x] **Integration with Google Gemini API - Lesson 11**:
  - Development of the independent module `gemini_api/client.py` and authentication setup using the `google-genai` SDK.
  - Configuration of the `gemini-2.5-flash` model for automated generation of summaries and academic descriptions, capped at 250 characters.
  - Protection of the API key (`API_KEY`) via a `.env` file using the `python-dotenv` library.

- [x] **Automation using Django Signals (`pre_save`)**:
  - Creation of the `signals.py` file within the `courses` app to monitor the `pre_save` event of the `Course` model.
  - Automatic generation of the `description` field using Artificial Intelligence during course creation whenever no description is provided.
  - Registration and activation of the signal listener through the `ready()` method in `apps.py` (`CoursesConfig`).

- [x] **MySQL Database Configuration - Lesson 09**:
  - Implementation of data persistence using the **MySQL** relational RDBMS.
  - Configuration of `School-API` to connect to the database via the `django.db.backends.mysql` engine.
  - Execution of migrations responsible for creating relational tables (`students`, `teachers`, `courses`).

- [x] **Student Management (`students`)**:
  - Implementation of the `Student` model using a foreign key (`ForeignKey`) for association with a course.
  - Enforcement of the integrity rule `on_delete=models.RESTRICT`, preventing the deletion of courses that have linked students.

- [x] **Teacher Management (`teachers`)**:
  - Development of the `teachers` app to manage instructor data (`name`, `date_of_birth`, and `hire_date`).
  - Implementation of Serializers and generic views (`Generics`) to expose full CRUD operations.

- [x] **Course Management (`courses`)**:
  - Development of the `courses` app featuring the `Course` model (`name`, `description`).
  - Implementation of a **Many-to-Many (NxN)** relationship between courses and teachers using `ManyToManyField(Teacher, related_name='courses')`.
  - Utilization of the Django ORM for automatic management of the join table in the relational database.
  - Update of the `Student` model to establish a **One-to-Many (1xN)** relationship with `Course`.
  - Implementation of the generic views `CourseCreateListView` and `CourseRetrieveUpdateDestroy`.

- [x] **Validation and Testing using Postman**:
  - Configuration and execution of HTTP requests (`GET`, `POST`, `PUT`, `DELETE`).
  - Setup of metadata via `Headers` and transmission of structured data in JSON format within the `Body`.
  - API operation testing following REST architectural standards.

### 🎨 Frontend (`student-management-vue`)

- [x] Initialization of the Vue.js 3 project with **Vue Router** support.
- [x] Installation and configuration of the **Axios** library.
- [x] Creation of the centralized API service (`src/services/api.js`) with CRUD methods.
- [x] Creation of the `HomeView.vue` page with the system's welcome screen.
- [x] Creation of the `StudentView.vue` page integrating interactive forms, date handling, and a student management table.
- [x] Configuration of **CORS** middleware in Django to allow requests from the local `:5173` port used by Vite/Vue.

---

## 🔑 Environment Variables & AI Configuration

To enable automatic course description generation using Google Gemini, create a `.env` file in the root directory of the Django project (`school-api/`) containing your API key:

```env
API_KEY="YourGoogleAIStudioKey"