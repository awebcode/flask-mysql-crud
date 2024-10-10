from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

# Initialize the Flask application
app = Flask(__name__)

# Function to create a connection to the MySQL database
def create_connection():
    connection = None
    try:
        # Connect to MySQL using provided credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Change this to your MySQL username
            password="mysql",  # Change this to your MySQL password
            port="3306",
        )
        print("MySQL connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to create the database and table if they do not exist
def create_database(connection):
    cursor = connection.cursor()
    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS flask_crud")
    cursor.execute("USE flask_crud")  # Use the new database
    # Create the users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100),
        phone VARCHAR(100)
    )
    """)
    cursor.close()

# Initialize the database connection and create database & table
db_connection = create_connection()
create_database(db_connection)

# Connect to the newly created database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="mysql",  # Change this to your MySQL password
    database="flask_crud",
    port="3306",
)

# Route to display all users
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)  # Use dictionary for easier access to column names
    cursor.execute("SELECT * FROM users")  # Fetch all users from the database
    users = cursor.fetchall()  # Get all records as a list of dictionaries
    cursor.close()  # Close the cursor
    return render_template('index.html', users=users)  # Render the index template with users data

# Route to show the add user form and handle form submission
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        cursor = db.cursor()
        # Insert new user into the database
        cursor.execute("INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)", 
                       (name, email, phone, password))
        db.commit()  # Commit the changes to the database
        return redirect(url_for('index'))  # Redirect to the index route
    return render_template('add.html')  # Render the add user form

# Route to edit an existing user
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        # Get updated form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        # Update user information in the database
        cursor.execute("UPDATE users SET name=%s, email=%s, password=%s, phone=%s WHERE id=%s", 
                       (name, email, password, phone, id))
        db.commit()  # Commit the changes
        return redirect(url_for('index'))  # Redirect to the index route
    
    # Fetch the current user data to pre-fill the form
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()  # Get the user record
    return render_template('edit.html', user=user)  # Render the edit user form with current user data

# Route to delete a user
@app.route('/delete/<int:id>')
def delete_user(id):
    cursor = db.cursor()
    # Delete user from the database
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()  # Commit the changes
    return redirect(url_for('index'))  # Redirect to the index route

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for easier troubleshooting
