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

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/awebcode/flask-mysql-crud.git
cd flask-mysql-crud

#Create a Virtual Environment
###It's a good practice to create a virtual environment for Python projects to manage dependencies.
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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
