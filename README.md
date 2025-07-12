## Product_review_system
Django REST Framework project with custom User (role-based), Products, ProductReviews.
## Setup
1. python -m venv env
2.  env\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate users
5. python manage.py makemigrations 
6. python manage.py migrate products
7. python manage.py makemigrations 
8. python manage.py createsuperuser
9. python manage.py runserver

API endpoints:
/api/users/
/api/products/
/api/reviews/


