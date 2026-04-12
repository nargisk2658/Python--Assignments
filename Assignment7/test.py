import psycopg2

# try to connect
try:
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
    print("Table created")

    # insert data
    cur.execute("INSERT INTO students (name, age) VALUES ('Nargis', 22);")
    conn.commit()
    print("Data inserted")

    # fetch data
    cur.execute("SELECT * FROM students;")
    data = cur.fetchall()

    print("All records:")
    for row in data:
        print(row)

    # close
    cur.close()
    conn.close()
    print("Done")

except Exception as e:
    print("Error:", e)