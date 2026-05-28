# Online Recruitment Management System using Python Django

A full-stack Smart Job Portal web application developed using Django, Python, HTML, CSS, JavaScript, Bootstrap, and SQLite.

The platform connects Candidates and Recruiters through an intelligent recruitment system with AI-based skill matching and applicant tracking features.

---

# 🚀 Features

## 🔐 Authentication System

* User Registration
* User Login & Logout
* Role-Based Authentication
* Secure Django Authentication

### Roles:

* Candidate
* Recruiter
* Admin

---

# 👨‍💼 Candidate Features

* View Available Jobs
* Search Jobs
* Filter Jobs by Location
* Apply for Jobs
* Upload Resume
* Track Applied Jobs
* AI Match Score Display
* Candidate Dashboard

---

# 🏢 Recruiter Features

* Recruiter Dashboard
* Post New Jobs
* Manage Posted Jobs
* Delete Jobs
* View Applicants
* View Uploaded Resumes
* AI Skill Match Percentage
* Shortlist Candidates

---

# 🛡 Admin Features

* Admin Dashboard
* Manage Platform Jobs
* Delete Fake Jobs
* Delete Applications
* Monitor Users & Applications

---

# 🤖 AI Features

## AI Skill Matching System

The system compares:

* Candidate Skills
* Required Job Skills

and generates:

* Match Percentage
* Applicant Suitability Score

Example:

```text
Required Skills:
Python, Django, SQL

Candidate Skills:
Python, SQL

Match Score:
66%
```

---

# 📂 Project Structure

```text
smartJobPortal/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── recruiter_dashboard.html
│   ├── candidate_dashboard.html
│   ├── apply_job.html
│   ├── admin_dashboard.html
│   └── post_job.html
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│   └── resumes/
│
├── smartjobportal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

# 🛠 Technologies Used

## Backend

* Python
* Django

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

## Database

* SQLite

## Other

* Django Authentication
* Bootstrap UI
* File Upload System

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

git clone https://github.com/bhakthan-avinash/Online-Recruitment-Management-System-using-Python-Django.git
---

## 2️⃣ Open Project Folder

cd Online-Recruitment-Management-System-using-Python-Django
---

## 3️⃣ Create Virtual Environment

python -m venv venv

---

## 4️⃣ Activate Virtual Environment

### Windows

venv\Scripts\activate


### Linux / Mac

source venv/bin/activate

---

## 5️⃣ Install Requirements

pip install -r requirements.txt

---

## 6️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate
---

## 7️⃣ Create Superuser

python manage.py createsuperuser

---

## 8️⃣ Run Server

python manage.py runserver

---

# 🌐 Open in Browser

http://127.0.0.1:8000/
```

---

# 📸 Main Pages

| Page                | URL                     |
| ------------------- | ----------------------- |
| Home                | `/`                     |
| Register            | `/accounts/register/`   |
| Login               | `/accounts/login/`      |
| Post Job            | `/post-job/`            |
| Recruiter Dashboard | `/recruiter-dashboard/` |
| Candidate Dashboard | `/candidate-dashboard/` |
| Admin Dashboard     | `/admin-dashboard/`     |

---

# 📌 Future Enhancements

* Email Notifications
* Real AI Resume Parsing
* Machine Learning Recommendations
* Chat System
* Video Interview Integration
* PostgreSQL Deployment
* Cloud Deployment (AWS/Render)

---

# 🎯 Learning Outcomes

This project demonstrates:

* Full Stack Web Development
* Django Framework
* SQL Database Integration
* Authentication Systems
* CRUD Operations
* File Upload Handling
* AI-Based Logic
* Bootstrap UI Design

---

👨 Developed By

Avinash

---

⭐ GitHub Repository

[Online Recruitment Management System using Python Django](https://github.com/bhakthan-avinash/Online-Recruitment-Management-System-using-Python-Django?utm_source=chatgpt.com)
