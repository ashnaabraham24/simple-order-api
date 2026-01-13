# Simple Order API

This is a simple backend API built using Django and Django REST Framework.

The project is backend-only and focuses on API logic and structure.
No frontend is included.

--------------------------------------------------

Features

- User model (id, name)
- Product model (id, name, price)
- Order model (user, product, quantity)
- One API endpoint to create an order
- Basic validation (quantity > 0)

--------------------------------------------------

Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

--------------------------------------------------

How to Run the Project

1. Clone the repository

git clone https://github.com/ashnaabraham24/order-api.git
cd order-api

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment (Windows)

venv\Scripts\activate

4. Install required packages

pip install django
pip install djangorestframework

5. Apply database migrations

python manage.py makemigrations
python manage.py migrate

6. Create a superuser (for admin access)

python manage.py createsuperuser

Use the admin panel to add User and Product data.
Admin URL: http://127.0.0.1:8000/admin/

7. Run the development server

python manage.py runserver

--------------------------------------------------

# API Usage

## Create Order

Method: POST
URL: /order/

Request Body (JSON)

{
  "user": 1,
  "product": 2,
  "quantity": 3
}

--------------------------------------------------

Testing

The API can be tested using:
- Postman
- curl

--------------------------------------------------

Notes

- Users and products are created via Django Admin
- Orders are created using the API endpoint
