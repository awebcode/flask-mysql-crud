# Flask MySQL CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built with Flask, using MySQL as the database and Jinja2 for templating. The application allows users to manage user information through a web interface.

## Features

- Add new users with name, email, password, and phone number.
- View a list of all users.
- Edit existing user details.
- Delete users from the database.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **MySQL**: A relational database management system.
- **Jinja2**: A templating engine for rendering HTML.

## Installation Guide

To set up the project locally, clone the repository:

```bash
git clone https://github.com/awebcode/flask-mysql-crud.git
cd flask-mysql-crud
Create a virtual environment to manage dependencies:

bash

python -m venv venv
Activate the virtual environment:

On Windows:
bash

venv\Scripts\activate
On macOS/Linux:
bash

source venv/bin/activate
Install the required packages:

bash

pip install -r requirements.txt
Set up the database by creating a new database in MySQL:

sql

CREATE DATABASE flask_crud;
Run the application:

bash

python app.py
Access the application by opening your web browser and navigating to http://127.0.0.1:5000.

Directory Structure
plaintext

flask-mysql-crud/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
└── static/
    └── styles.css
Instructions for Cloning the Repository
If you clone the repository, make sure to create a new virtual environment and install the dependencies. After cloning the repository, run the following commands:

Create a virtual environment:

bash

python -m venv venv
Activate the virtual environment:

On Windows:
bash

venv\Scripts\activate
On macOS/Linux:
bash

source venv/bin/activate
Install the required packages:

bash

pip install -r requirements.txt
Contributing
Feel free to fork the repository and submit pull requests for any improvements or additional features.

License
This project is licensed under the MIT License. See the LICENSE file for details.


