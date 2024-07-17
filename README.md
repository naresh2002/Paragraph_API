# Paragraph_API

# .env
DATABASE_NAME={{DATABASE_NAME}}  
DATABASE_USER={{DATABASE_USER}}  ``` Generally "postgres"```  
DATABASE_PASS={{DATABASE_PASS}}  

# Installation requirements
1. Decouple to get env variables configuration from .env file  
   ` pip install python-decouple `
2. Django, djangorestframework and psycopg2  
   ` pip install django djangorestframework psycopg2-binary `
3. Simple_JWT for tokenisation  
   ` pip install djangorestframework-simplejwt ` 

# HOW TO TEST PROJECT
1. Clone the repository in your local.  
   ` git clone https://github.com/naresh2002/Paragraph_API.git `
2. Create .env file inside parent folder (Paragraph_API) using  
   ` touch .env `
3. Write .env file as  
   DATABASE_NAME={{DATABASE_NAME}}  
   DATABASE_USER={{DATABASE_USER}}  
   DATABASE_PASS={{DATABASE_PASS}}
4. Go to your postgres shell and create a new database as {{DATABASE_NAME}}  
   a. To enter postgres shell in terminal for Ubuntu (varies for different OS)  
   ` sudo -u postgres psql `  
   b. In postgres shell  
   ` CREATE DATABASE {{DATABASE_NAME}}; `
5. Make migration  
   ` python manage.py makemigrations `  
6. Migrate schemas to DB  
   ` python manage.py migrate `  
7. Start the server.  
   ` python manage.py runserver `
