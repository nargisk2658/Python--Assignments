# Assignment 9 - Django REST API

## About Project

This is a simple Django REST API project.
I created this project to understand how APIs work in Django using Django REST Framework.

In this project, I made a User API where we can add, view, update and delete users.

---

## Features

* Add new user
* View all users
* View single user
* Update user details
* Delete user

---

## User Fields

* name
* email
* age

I also added a small validation for age.

---

## API Endpoints

* GET /api/users/ → get all users
* POST /api/users/ → create user
* GET /api/users/<id>/ → get single user
* PUT /api/users/<id>/ → update user
* DELETE /api/users/<id>/ → delete user

---

## How to Run

1. Install Django and DRF
2. Run migrations
3. Start server

Commands:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

---

## What I Learned

* How to create a Django project
* How to create an app
* How to use serializers
* How to use class-based views
* How to connect URLs

---

## Conclusion

This project helped me understand the basics of Django REST API and how backend APIs work.
