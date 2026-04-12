# PostgreSQL + Python Basic Assignment

## What I did

In this assignment, I connected Python with PostgreSQL database and performed some basic operations like creating a table, inserting data and fetching records.

## Steps performed

* Connected to PostgreSQL using psycopg2
* Created a table named `students`
* Inserted one record into the table
* Retrieved and displayed the data
* Closed the connection

## Requirements

* Python installed
* PostgreSQL installed and running
* psycopg2 library

To install psycopg2:

```
pip install psycopg2-binary
```

## How to run

1. Open terminal
2. Go to project folder
3. Run:

```
python test.py
```

## Output

The program connects to the database, creates a table (if not exists), inserts a record and prints all records.

## Note

Make sure PostgreSQL server is running and correct password is used in the code.

