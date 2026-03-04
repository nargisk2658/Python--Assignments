# Flask User Registration System

This is a simple user registration system built using:

- Flask
- Flask-WTF
- WTForms
- SQLAlchemy
- SQLite Database

The application allows users to register with proper form validation and stores the data in a database.

---

## Features

- User Registration Form
- Form Validation using Flask-WTF
- Confirm Password Validation
- Data stored in SQLite database
- Success page after registration
- Error handling using try-except
- CSRF protection using Secret Key

---

## Project Structure

registration_system/

│── app.py  
│── config.py  
│── models.py  
│── forms.py  
│── requirements.txt  
│── README.md  
└── templates/  
  │── base.html  
  │── register.html  
  │── success.html  

---

## Installation Steps

1. Install required packages:

pip install -r requirements.txt

OR

pip install flask flask-wtf flask-sqlalchemy email-validator

2. Run the application:

python app.py

3. Open your browser and go to:

http://127.0.0.1:5000/

---

## Database

- The database file (users.db) is automatically created.
- User registration data is stored in SQLite database.

---

## Author

Name: Nargis Khatoon  
Course: MCA  
