# Todo API (Django REST Framework)

### ✏ Description
- This API is for record history where we visit

### ⚙ Envirionments (python 3.8.0)
> pip install django==3.1.7

> pip install djangorestframework==3.12.4

> pip install django-dotenv==1.4.2

❗ And, you have to create `.env` file in root.
```
Project tree
------------
root
├── .env            ### here
├── README.md
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── history
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── user
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
then, please insert secret key (you can get at https://djskgen.herokuapp.com/)
```
SECRET_KEY="value"
DEBUG=True
```
<br>

### 📃 API Descriptions

<b>User</b>
- GET "users/" - User list read
- POST "users/" - User create
- GET "users/<int:user_id>" -User detail read
- PATCH "users/<int:user_id>" - User update
- DELETE "users/<int:user_id>" - User delete

<b>History</b>
- GET "histories/" - History list read
- POST "histories/" - History create
- PATCH "histories/<int:history_id>" - History update
- DELETE "histories/<int:history_id>" - History delete
- GET "histories/search/?query=<location_keyword>" - Location search(naver search api, get 5 results)
<br>

### ▶ Execution
> pip install httpie
```python
python manage.py makemigrations

python manage.py migrate

# execute django web server
python manage.py runserver

# if you see error "No such table Todo", 
## python manage.py makemigrations todo
## python manage.py migrate
## python manage.py runserver

""" in another cmd """
# please user httpie for test

```
<br>
