# Importing required library
import psycopg2


# Function: getConnection()
# Purpose: Establishes and returns a database connection

def getConnection():
    try:
        connection = psycopg2.connect(
            database="demodb",
            user="postgres",
            password="Admin",
            host="localhost",
            port="5432"
        )
        print("Database connected successfully.")
        return connection

    except Exception as e:
        print("Error while connecting to database:", e)
        return None



# Function: table()
# Purpose: Creates employees table if it does not exist
# SQL Operation: CREATE TABLE

def table():
    conn = getConnection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            Name TEXT,
            ID INT,
            Age INT);""")

        conn.commit()
        print("Table created successfully.")

    except Exception as e:
        print("Error while creating table:", e)

    finally:
        cursor.close()
        conn.close()


# Function: getAll()
# Purpose: Retrieves and displays all records
# SQL Operation: SELECT

def getAll():
    conn = getConnection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        records = cursor.fetchall()

        print("\nEmployee Records:")
        print("-------------------")

        for row in records:
            print(f"Name: {row[0]}, ID: {row[1]}, Age: {row[2]}")

    except Exception as e:
        print("Error while fetching records:", e)

    finally:
        cursor.close()
        conn.close()



# Main execution

if __name__ == "__main__":
    table()      # Create table
    getAll()     # Display all records
