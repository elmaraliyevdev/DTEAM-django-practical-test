# DTEAM - Django Developer Practical Test

## **Overview**
This is a Django-based **CV Management System** built as part of the DTEAM Practical Test.  
It includes **Django REST Framework, PostgreSQL, Celery, OpenAI integration**, and is fully **Dockerized**.

---

## **Installation & Setup**
### ** Install Dependencies**
#### **Using Poetry & Pyenv**
Ensure you have **Python 3.11** installed and set up using `pyenv`:

```sh
pyenv install 3.11
pyenv local 3.11
```

Then, install dependencies using **Poetry**:

```sh
poetry install
```

---

### ** Run the Application Locally**
1. Create a `.env` file:

```sh
cp .env.example .env
```

2. Apply migrations:

```sh
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

3. Start the Django server:

```sh
poetry run python manage.py runserver
```

Now, visit **http://127.0.0.1:8000/** 🚀

---

### **3️⃣ Run the Application with Docker**
```sh
docker compose up -d --build
```

To apply migrations inside the container:

```sh
docker compose exec web poetry run python manage.py migrate
```

---

## **Features Implemented**
### **Task 1: Django Fundamentals**
- Created a `CVProject` Django app.
- Implemented `CV` model with `firstname, lastname, skills, projects, bio, contacts`.
- Added list & detail views with basic styling.
- Created test cases.

### **Task 2: PDF Generation**
- Integrated **WeasyPrint** for HTML-to-PDF conversion.
- Added "Download PDF" button to CV detail page.

### **Task 3: REST API**
- Created **CRUD API** for `CV` using Django REST Framework.
- Implemented API tests.

### **Task 4: Middleware & Logging**
- Added `RequestLog` model to log **HTTP requests**.
- Implemented **custom middleware** for logging.
- Created `/logs/` page to display recent requests.

### **Task 5: Template Context Processors**
- Implemented `settings_context` to inject **Django settings** into templates.
- Created a `/settings/` page to display key settings.

### **Task 6: Docker**
- Created `Dockerfile` and `docker-compose.yml`.
- Switched from SQLite to PostgreSQL.
- Stored credentials in `.env` file.

### **Task 7: Celery & Emailing PDFs**
- Integrated **Celery with Redis**.
- Added "Send CV to Email" feature.
- Configured SMTP settings.

### **Task 8: OpenAI Integration**
- Integrated **OpenAI GPT**.
- Added an API for **career advice based on CV**.

---

## **Testing**
### **Run Unit Tests**
```sh
poetry run python manage.py test
```

### **API Testing (Using cURL)**
```sh
curl -X GET http://127.0.0.1:8000/api/cvs/
```

---

To **restart services**:
```sh
docker-compose restart
```