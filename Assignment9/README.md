# Django REST API Project (Assignment 12)

This is a simple Django REST API project I created as part of my assignment.

## What this project does

* Connects to a Django backend
* Creates a Student model (name, age, email)
* Allows:

  * Viewing all students (GET request)
  * Adding a new student (POST request)

## Tools used

* Python
* Django
* Django REST Framework
* django-filter (version 2.4.0)

## How to run the project

1. Open terminal and go to project folder

2. Install required libraries:

```
pip install django
pip install djangorestframework
pip install django-filter==2.4.0
```

3. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

4. Start server:

```
python manage.py runserver
```

5. Open in browser:

```
http://127.0.0.1:8000/api/students/
```

## API Endpoints

* GET all students
  `/api/students/`

* Add new student
  `/api/add/`

Example data for POST:

```
{
  "name": "Nargis",
  "age": 22,
  "email": "nargis@email.com"
}
```

## Notes

* This is a basic project for learning REST APIs
* I tried to keep the code simple and easy to understand
* I wrote the final version after practicing different approaches

