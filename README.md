# Backend-Development-Mini-Project-1-Jas_Simarjeet_Singh
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-O3YcVon)
# Backend Development - Mini Project-1
# Social Media App

The backend for a social media platform that allows users to create accounts, follow others, send messages, like and comment on posts, and receive real-time notifications. Built using Flask and SQL, this platform provides an engaging way for users to interact and connect with each other.

## Table of Contents

- Like App
- Comment App

## Features

- **Likes**: Users can like/unlike posts.
- **Comments**: Users can comment on posts and reply to comments.

## Technologies

- **Frontend**: .........
- **Backend**: Flask
- **Database**: SQl, SQLalchemy

## Getting Started

### Prerequisites

- Python 3.12.4 and pip 24.2 installed on your machine
- Check version of python and pip on your machine

    ```bash
    python --version
    pip --version
- MySQL instance running locally or in the cloud
- [click here for download python](https://www.python.org/downloads/release/python-3124/)
- [click here for download MySQL](https://dev.mysql.com/downloads/workbench/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Faculty-of-Technology-DU/backend-development-mini-project-1-jassimarjeet.git

   cd social_media_app

2. Open MySQL Workbench and create the database:
    ```sql
    CREATE DATABASE social_media_app_db

3. Configure the Application:

    In the root directory of the project, open the config folder and find the config.py file.

    - Replace {password} with your MySQL password.
    - Replace python_dir with the path to your Python virtual environment.

    
    ```bash
    /path/to/your/venv/bin/python3  # For Mac/Linux
    venv\\Scripts\\python.exe       # for Windows
    
4. Set Up the Virtual Environment:
    
    In your command prompt/terminal, run the following commands:
    - For Windows users:
        ```bash
        python -m venv venv
        venv\\Scripts\\activate
        pip install -r requirements.txt
        cd shared
        set FLASK_APP=app
        flask db init
        flask db migrate
        flask db upgrade
    - For Mac users:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        cd shared
        export FLASK_APP=app
        flask db init
        flask db migrate
        flask db upgrade

5. Run the Flask Application:

    After setting up, you can run the Flask application by executing the following command in the project root directory::
    - Open terminal in project **root directory** and run this command
    ```bash
    python app_runner.py    # for Windows
    python3 app_runner.py   # for mac and linux

6. Testing with Postman:
    
    Install [Postman](https://www.postman.com/downloads/) to test the API endpoints.
    - [Learn how to use Postman to test your API](https://learning.postman.com/docs/designing-and-developing-your-api/testing-an-api/)

7. Response Data: 
    
    If you're using the social media app and would like to interact with the API, here's a guide to the data you should pass in POST requests for various actions. To make this easier for you, I have attached a Postman Collection, which contains all the endp
