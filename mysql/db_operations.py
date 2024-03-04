import mysql.connector
from mysql.connector import Error

def execute_sql_commands():
    """Connects to MySQL and executes a series of SQL commands."""
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='mysql-server',  # Name of the MySQL container
            user='root',          # MySQL user
            password='my-secret-pw',  # Password for the MySQL user
            database='mysql'      # Default database to use
        )

        if connection.is_connected():
            print('Successfully connected to MySQL database')
            cursor = connection.cursor()

            # Create a new database named 'testdb'
            cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
            print("Database 'testdb' created successfully.")

            # Use the new database
            cursor.execute("USE testdb")

            # Create a new table named 'employees'
            cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), position VARCHAR(255))")
            print("Table 'employees' created successfully.")

            # Insert a new employee into the 'employees' table
            cursor.execute("INSERT INTO employees (name, position) VALUES ('John Doe', 'Software Engineer')")
            connection.commit()
            print("New employee inserted successfully.")

            # Select all employees from the 'employees' table
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()

            print("Employees:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    execute_sql_commands()
