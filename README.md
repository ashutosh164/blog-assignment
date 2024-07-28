Blog Application with Django and Django REST Framework

Introduction:
This is a simple blog application built using Django and Django REST Framework (DRF). 
The application includes basic CRUD functionalities for blog posts and comments, 
and integrates token-based authentication to ensure that only authenticated users can create, update, or delete posts and comments.

Requirements:
Python 3.x
Django 3.x or higher
Django REST Framework 3.x or higher

Installation
Clone the repository:
1. git clone https://github.com/ashutosh164/blog-assignment.git
2. cd blogproject

Create and activate a virtual environment:
1. python3 -m venv venv
2. source venv/bin/activate

Install the required packages:
1. pip install -r requirements.txt

Apply migrations:
1. python manage.py migrate
   
Create a superuser:
1. python manage.py createsuperuser
   
Run the development server:
1. python manage.py runserver

APIs
Post API Views:

List: GET /api/posts/
Create: POST /api/posts/
Retrieve: GET /api/posts/{id}/
Update: PUT /api/posts/{id}/
Delete: DELETE /api/posts/{id}/

User Authentication
Token Authentication

Use Django REST Framework Token for authentication.
NOTE:- Only authenticated users can create, update, or delete posts and comments.

Run main.py for get the data
1. ctrl + shift + f10

Test the code using command:
1. coverage run --omit='*/venv/*' manage.py test 



