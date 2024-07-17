# Paragraph_API

A REST API in Django that performs user signup, login along with basic operations on paragraphs and words.  
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
4. **drf_yasg** for Swagger documentation  
    ```bash
    pip install drf-yasg
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

   ``` /api/signup/ ```  

   Request Body:  
   ```json
   {
   "name": "Naresh Kumar",
   "email": "naresh@gmail.com",
   "dob": "2000-01-01",
   "password": "Naresh@12345"
   }
   ```  

   Curl Command:  
   ```bash
   curl -X POST http://localhost:8000/api/signup/
   -H "Content-Type: application/json"
   -d '{
   "name": "Naresh Kumar",
   "email": "naresh@gmail.com",
   "dob": "2000-01-01",
   "password": "Naresh@12345"
   }'
   ```

2. **Login** [POST]  

   ``` /api/login/ ```  

   Request Body:  
   ```json
   {
   "email": "naresh@gmail.com",
   "password": "Naresh@12345"
   }
   ```  

   Curl Command:  
   ```bash
   curl -X POST http://localhost:8000/api/login/
   -H "Content-Type: application/json"
   -d '{
   "email": "naresh@gmail.com",
   "password": "Naresh@12345"
   }'
   ```

   Response:  
   ```json
   {
   "refresh": "<refresh_token>",
   "access": "<access_token>"
   }
   ```

   **Adding Bearer Token in Swagger UI**  
   To use endpoints that require authentication, you need to include the access token in the Authorization header.

   Click on the Authorize button in the Swagger UI.  
   Enter the token in the following format:  
   Bearer <access_token>  
   Click Authorize and then Close.  

3. **Current User** [GET]  

   ``` /api/current_user/ ```  

   Headers:  
   Authorization: Bearer <access_token>  

   Curl Command:  
   ```bash
   curl -X GET http://localhost:8000/api/current_user/
   -H "Authorization: Bearer <access_token>"
   ```

4. **Add Paragraph** [POST]  

   ``` /api/add_paragraph/ ```  

   Request Body:  
   ```json
   {
   "paragraph": "This is a sample paragraph."
   }
   ```

   Headers:  
   Authorization: Bearer <access_token>  

   Curl Command:  
   ```bash
   curl -X POST http://localhost:8000/api/add_paragraph/
   -H "Content-Type: application/json"
   -H "Authorization: Bearer <access_token>"
   -d '{
   "paragraph": "This is a sample paragraph."
   }'
   ```

5. **Search Word** [GET]  

   ``` /api/search_word/{word}/ ```  

   Headers:  
   Authorization: Bearer <access_token>  

   Curl Command:  
   ```bash
   curl -X GET http://localhost:8000/api/search_word/sample/
   -H "Authorization: Bearer <access_token>"
   ```

6. **Logout** [POST]  

   ``` /api/logout/ ```  

   Headers:  
   Authorization: Bearer <access_token>  

   Curl Command:  
   ```bash
   curl -X POST http://localhost:8000/api/logout/
   -H "Authorization: Bearer <access_token>"
   ```

## Swagger UI Documentation
To view and interact with the API using Swagger UI, follow these steps:

Run the Django server:
```bash
python manage.py runserver
```
Open a web browser and go to:
```
http://localhost:8000/swagger/
```
In Swagger UI, you will see all the available endpoints, their methods, request parameters, and responses. You can also interact with these endpoints directly from the UI.

## Summary  

This project includes endpoints for user authentication, adding paragraphs, searching for words, and managing user sessions. All sensitive endpoints require an access token, which is obtained upon logging in. This token must be included in the Authorization header as "Bearer <access_token>" for subsequent requests.  

Make sure to install all required packages and set up the environment as described. Use the provided curl commands or Swagger UI to test the API endpoints.  
