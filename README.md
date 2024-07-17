# Paragraph_API

A REST API in Django that performs basic CRUD (Create, Read, Update, Delete) operations on paragraphs and words.  
Utilizes **Django Rest Framework** with **SimpleJWT** for token-based authentication.  
Ensures proper request data validation and secure user authentication.  

The project is designed to manage user-submitted paragraphs, providing endpoints to create, read, and search for words within these paragraphs. Additionally, it supports user registration, login, and secure session management.

## Installation Requirements

1. **Decouple** to get env variables configuration from .env file  
    ```bash
    pip install python-decouple
    ```
2. **Django**, **djangorestframework**, and **psycopg2-binary**  
    ```bash
    pip install django djangorestframework psycopg2-binary
    ```
3. **SimpleJWT** for tokenisation  
    ```bash
    pip install djangorestframework-simplejwt
    ```

## How to Run This Project

1. Clone the repository in your local machine.  
    ```bash
    git clone https://github.com/naresh2002/Paragraph_API.git
    ```

2. Navigate to the project directory and create a `.env` file inside the parent folder (Paragraph_API).  
    ```bash
    cd Paragraph_API
    touch .env
    ```

3. Write the following configuration in the `.env` file:  
    ```plaintext
    DATABASE_NAME={{DATABASE_NAME}}
    DATABASE_USER={{DATABASE_USER}}
    DATABASE_PASS={{DATABASE_PASS}}
    ```

4. Go to your PostgreSQL shell and create a new database as `{{DATABASE_NAME}}`.  
    a. To enter PostgreSQL shell in terminal for Ubuntu (varies for different OS):  
    ```bash
    sudo -u postgres psql
    ```
    b. In PostgreSQL shell:  
    ```sql
    CREATE DATABASE {{DATABASE_NAME}};
    ```

5. Make migrations:  
    ```bash
    python manage.py makemigrations
    ```

6. Migrate schemas to the database:  
    ```bash
    python manage.py migrate
    ```

7. Start the server:  
    ```bash
    python manage.py runserver
    ```

8. Open a new terminal and test the endpoints given below using curl commands.

## Endpoints

1. **Signup** [POST]  
    ```http://127.0.0.1:8000/api/signup/```  
    curl command:  
    ```bash
    curl -X POST http://localhost:8000/api/signup/ \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Naresh Kumar",
        "email": "naresh@gmail.com",
        "dob": "2000-01-01",
        "password": "Naresh@12345"
    }'
    ```

2. **Login** [POST]  
    ```http://127.0.0.1:8000/api/login/```  
    curl command:  
    ```bash
    curl -X POST http://localhost:8000/api/login/ \
    -H "Content-Type: application/json" \
    -d '{
        "email": "naresh@gmail.com",
        "password": "Naresh@12345"
    }'
    ```

3. **Current User** [GET]  
    ```http://127.0.0.1:8000/api/current_user/```  
    curl command:  
    ```bash
    curl -X GET http://localhost:8000/api/current_user/ \
    -H "Authorization: Bearer <your_access_token>"
    ```

4. **Add Paragraph** [POST]  
    ```http://127.0.0.1:8000/api/add_paragraph/```  
    curl command:  
    ```bash
    curl -X POST http://localhost:8000/api/add_paragraph/ \
    -H "Authorization: Bearer <your_access_token>" \
    -H "Content-Type: application/json" \
    -d '{
        "paragraph": "This is a sample paragraph to be added."
    }'
    ```

5. **Search Word** [GET]  
    ```http://127.0.0.1:8000/api/search_word/{word}/```  
    curl command:  
    ```bash
    curl -X GET http://localhost:8000/api/search_word/sampleword/ \
    -H "Authorization: Bearer <your_access_token>"
    ```

6. **Logout** [POST]  
    ```http://127.0.0.1:8000/api/logout/```  
    curl command:  
    ```bash
    curl -X POST http://localhost:8000/api/logout/ \
    -H "Authorization: Bearer <your_access_token>"
    ```

## Notes

- Replace `{{DATABASE_NAME}}`, `{{DATABASE_USER}}`, and `{{DATABASE_PASS}}` with your actual PostgreSQL database name, user, and password in the `.env` file.
- Replace `<your_access_token>` with the actual JWT access token you receive after logging in.
