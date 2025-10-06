# 📝 Notes App
A **full-featured Django Notes Application** built with scalability, security, and clean architecture.  
Users can sign up, verify their email, and securely manage personal notes — all running in a **Dockerized** environment deployed on **Render** with **Gunicorn** and **SendGrid integration**.

## 🚀 Features
### 🔐 Authentication & Security
- User signup, login, and logout  
- Email verification via **SendGrid**  
- Password reset through email  
- Strong SSL, HSTS, and secure cookie configurations  

### 🗒️ Notes & Comments
- Create, edit, and delete personal notes  
- Add and manage comments on notes  
- Search and filter notes efficiently  
- Responsive, minimal user interface  

### ⚙️ APIs (Django REST Framework)
- RESTful API endpoints for Notes and Comments  
- JSON-based responses for easy integration  
- Authentication and permission handling  

### 🧩 Infrastructure & Deployment
- **Dockerized** setup for portability  
- **Gunicorn** as WSGI production server  
- **Render** deployment with environment-based configs  
- Configurable `.env` for all sensitive values  

## 🏗️ Tech Stack
| Layer           | Technology                                           |
| --------------- | ---------------------------------------------------- |
| Backend         | Django 5.x                                           |
| APIs            | Django REST Framework                                |
| Server          | Gunicorn + Docker                                    |
| Database        | SQLite (development) / PostgreSQL (production-ready) |
| Deployment      | Render                                               |
| Email Service   | SendGrid                                             |
| Version Control | Git & GitHub                                         |

## 🐳 Docker Setup

Build and run locally:
```bash
docker-compose up --build
```
App will be available at: http://localhost:8000

## 🌍 Deployment (Render)

1. Connect your GitHub repo on Render

2. Choose Docker as environment type

3. Add all environment variables from .env

4. Deploy and access your live site

**Live App**: https://notes-app-ysaa.onrender.com

## 📫 Email Verification & Password Reset

- Uses SendGrid for all outgoing emails (signup verification, password reset).

- Make sure DEFAULT_FROM_EMAIL matches a verified SendGrid sender.

## 🔍 Search & REST APIs

- Search notes by title or content.

- REST API endpoints (via DRF):

  - /api/notes/

  - /api/comments/
Example Usage:
```bash
GET /api/notes/
POST /api/notes/ { "title": "Test", "content": "Hello World" }
```
## 🧠 Author

### Yuvraj Rana

💻 **CS Undergraduate** | **Django Developer**
singh.yuvrajrana256@gmail.com
