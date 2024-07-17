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

## Authentication

After logging in, you will receive both a refresh token and an access token. The access token is required for authenticating requests to protected endpoints. 

### Using Tokens with cURL

Include the access token in the `Authorization` header as follows:
```bash
-H "Authorization: Bearer <your_access_token>"
```
### Using Tokens with Postman
After logging in, copy the access token from the response.
For each protected endpoint request:
Open Postman and select the endpoint.
Go to the "Authorization" tab.
Select "Bearer Token" from the "Type" dropdown.
Paste the access token into the "Token" field.

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
    Response example :  
    ```bash
   {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMTMwNDQ3MiwiaWF0IjoxNzIxMjE4MDcyLCJqdGkiOiI2Mzg5MTk5ZmEzNGM0OGJlOTNhZmNiNWRhMmVjOTU5NyIsInVzZXJfaWQiOjF9.oo3v-f8EY73DnmEFYovVxJ9yguV8QbrsVBNRpFA6E70",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxMjIxNjcyLCJpYXQiOjE3MjEyMTgwNzIsImp0aSI6IjAxYWI2YTUyOGZkNTRlNjQ4MTU5ZGEzYjJhNDgzZDhjIiwidXNlcl9pZCI6MX0.e5C57PJzer4O5GPRt2HxksHSnXVOqazeXJtuxVgVvqY"
   }
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
    (a) Example 1:  
    ```bash
    curl -X POST http://localhost:8000/api/add_paragraph/ \
    -H "Authorization: Bearer <your_access_token>" \
    -H "Content-Type: application/json" \
    -d '{
        "paragraph": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam atlectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque."
    }'
    ```  
    (b) Example 2:  
    ```bash
    curl -X POST http://localhost:8000/api/add_paragraph/ \
    -H "Authorization: Bearer <your_access_token>" \
    -H "Content-Type: application/json" \
    -d '{
        "paragraph": "Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id."
    }'
    ```

5. **Search Word** [GET]  
    ```http://127.0.0.1:8000/api/search_word/{word}/```  
    curl command:  
    ```bash
    curl -X GET http://localhost:8000/api/search_word/sampleword/ \
    -H "Authorization: Bearer <your_access_token>"
    ```   
    (a) Example 1:  
    ```bash
    curl -X GET http://localhost:8000/api/search_word/lorem/ \
    -H "Authorization: Bearer <your_access_token>"
    ```  
    (b) Example 2:  
    ```bash
    curl -X GET http://localhost:8000/api/search_word/Maecenas/ \
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
