import psycopg2

# try to connect
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

print("Connected!")

cur = conn.cursor()

# create table
cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name TEXT, age INT);")

# insert data
name = "Nargis"
age = 22
cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))

conn.commit()

# fetch data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("All records:")
for row in rows:
    print(row)

conn.close()
print("Done")
