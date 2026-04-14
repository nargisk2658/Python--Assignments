# Django REST API - User Management

## 📌 Project Overview

This project is a simple Django REST API that allows basic operations on users.
It is built to understand how Django REST Framework works using class-based views.

The API supports:

* Creating a new user
* Viewing all users
* Retrieving a single user
* Updating user details
* Deleting a user

---

## 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite (default database)

---

## 📂 Project Structure

* `users/` → contains models, views, serializers
* `models.py` → defines User model
* `serializers.py` → converts model data to JSON
* `views.py` → handles API logic using class-based views
* `urls.py` → defines API routes

---

## 👤 User Model Fields

* `name` → stores user's name
* `email` → unique email for each user
* `age` → integer value for age

Basic validation is applied to ensure:

* Email is unique
* Age cannot be negative

---

## 🔗 API Endpoints

### 1. Get all users / Create user

`GET /api/users/` → returns list of users
`POST /api/users/` → creates a new user

### 2. Get / Update / Delete single user

`GET /api/users/<id>/`
`PUT /api/users/<id>/`
`DELETE /api/users/<id>/`

---

## ▶️ How to Run the Project

1. Install dependencies:

```
python -m pip install django djangorestframework
```

2. Navigate to project folder:

```
cd myproject
```

3. Apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

4. Run server:

```
python manage.py runserver
```

5. Open in browser:

```
http://127.0.0.1:8000/api/users/
```

---

## 💡 Learning Outcome

Through this project, I learned:

* How to create Django apps
* How to build REST APIs using Django REST Framework
* How to use class-based views like ListCreateAPIView and RetrieveUpdateDestroyAPIView
* How serializers work for data validation and conversion

---

## ✅ Conclusion

This project demonstrates a basic but functional REST API with proper structure and validation.
It follows the required approach using class-based views and clean organization of files.
