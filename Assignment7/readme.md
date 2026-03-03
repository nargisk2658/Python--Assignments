# Implementing Database Operations using Python

## Requirements
- Python 3.x
- PostgreSQL installed
- psycopg2 library

## Setup Instructions

### 1. Create Virtual Environment
python -m venv venv

### 2. Activate Virtual Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install psycopg2
pip install psycopg2

### 4. Create Database
Open PostgreSQL and create a database named:
testdb

### 5. Run the Script
python database_operations.py

## Description
- getConnection() → Connects to PostgreSQL database
- table() → Creates employees table
- getAll() → Retrieves and displays all employee records
