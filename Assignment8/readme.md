# Flask Registration System (Flask-WTF + SQLAlchemy)

## 📌 Project Overview

This project is a complete Registration System built using **Flask**, **Flask-WTF**, and **SQLAlchemy**.

The application allows users to register using a form with proper validation and stores the registration data in a SQLite database.

This project demonstrates practical implementation of:

* Flask Routing
* Template Rendering (Jinja2)
* Flask-WTF Forms
* WTForms Validators
* CSRF Protection
* SQLAlchemy ORM
* SQLite Database Integration
* Error Handling

---

## 🛠 Technologies Used

* Python 3
* Flask
* Flask-WTF
* WTForms
* Flask-SQLAlchemy
* SQLite
* HTML (Jinja2 Templates)

---

## 📂 Project Structure

project_folder/

├── app.py
├── users.db (auto-created database file)
├── README.md
└── templates/
  ├── register.html
  └── success.html

---

## 🚀 Features

✔ User Registration Form
✔ Form Validation using Flask-WTF
✔ Confirm Password Validation
✔ Email Format Validation
✔ Minimum Password Length Validation
✔ CSRF Protection
✔ SQLite Database Storage
✔ Error Handling with Try-Except
✔ Success Page after Registration

---

## 🔐 Form Validations Implemented

* Name must not be empty
* Email must be valid format
* Password must be at least 6 characters
* Confirm Password must match Password
* Duplicate email prevented using unique constraint

---

## 🗄 Database Details

* Database: SQLite
* File Name: `users.db`
* ORM Used: SQLAlchemy
* Table Created: `User`
* Fields:

  * id (Primary Key)
  * name
  * email (Unique)
  * password

The database file is automatically created when the application runs for the first time.

---

## ▶ How to Run the Project

### Step 1: Install Required Packages

Open terminal inside project folder and run:

```
pip install flask flask-wtf flask-sqlalchemy email-validator
```

---

### Step 2: Run the Application

```
python app.py
```

---

### Step 3: Open in Browser

Go to:

```
http://127.0.0.1:5000
```

---

## ⚠ Important Configuration

The application includes:

```
app.config['SECRET_KEY'] = 'mysecretkey'
```

This is required for CSRF protection in Flask-WTF.

---

## 📌 Learning Outcomes

Through this project, the following concepts were implemented and understood:

* Difference between raw form handling and Flask-WTF forms
* How to create and validate forms using WTForms
* How to define models using SQLAlchemy
* How to persist data in SQLite database
* How to protect forms using CSRF token
* How to structure a Flask project professionally



## 📝 Note

This project is developed for learning purposes as part of the Flask module assignment. It demonstrates core backend concepts required for building real-world web applications.
