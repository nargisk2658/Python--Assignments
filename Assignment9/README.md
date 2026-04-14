# Django REST API - User Management

## 📌 Project Description

This project is a simple Django REST API for managing users.
It allows us to create, view, update, and delete user data using API endpoints.

I created this project to understand how Django REST Framework works with models, serializers, and class-based views.

---

## 🛠 Technologies Used

* Python
* Django
* Django REST Framework

---

## 📂 Project Structure

* users/ → contains models, views, serializers
* urls.py → handles API routes
* manage.py → Django project runner

---

## ⚙️ Setup Instructions

1. Clone or download the project

2. Install required packages:
   pip install django djangorestframework

3. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Run the server:
   python manage.py runserver

5. Open browser:
   http://127.0.0.1:8000/

---

## 🔗 API Endpoints

### 1. Get all users

GET /api/users/

### 2. Create a user

POST /api/users/

Example JSON:
{
"name": "Nargis",
"email": "[nargis@gmail.com](mailto:nargis@gmail.com)",
"age": 22
}

---

### 3. Get single user

GET /api/users/<id>/

---

### 4. Update user

PUT /api/users/<id>/

---

### 5. Delete user

DELETE /api/users/<id>/

---

## ✅ Features

* Create new user
* View all users
* Update user details
* Delete user
* Basic validation (age must be 18+)

---

## 💡 What I Learned

* How to create models in Django
* How serializers convert data to JSON
* How class-based views work (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
* How to test APIs using browser/Postman

---

## 👩‍💻 Author

Nargis Khatoon
